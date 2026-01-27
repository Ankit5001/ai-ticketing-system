from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import joblib
import os
import re
from . import models, schemas, database

# 1. Initialize App
app = FastAPI(title="AI Ticketing System")
models.Base.metadata.create_all(bind=database.engine)

# 2. Mount Static Folder (Serves HTML, CSS, JS)
# This tells FastAPI: "Look inside the 'static' folder for website files"
script_dir = os.path.dirname(__file__)
static_path = os.path.join(os.path.dirname(script_dir), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# 3. Load Models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPT_MODEL_PATH = os.path.join(BASE_DIR, "models/ticket_pipeline.joblib")
PRIO_MODEL_PATH = os.path.join(BASE_DIR, "models/priority_pipeline.joblib")

dept_model = None
prio_model = None

try:
    dept_model = joblib.load(DEPT_MODEL_PATH)
    prio_model = joblib.load(PRIO_MODEL_PATH)
    print("✅ All AI Brains Loaded Successfully")
except Exception as e:
    print(f"⚠️ Model Loading Error: {e}")

# 4. Cleaning Function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# 5. API Endpoint (The Brain)
@app.post("/predict_ticket/", response_model=schemas.TicketOutput)
def create_ticket(ticket: schemas.TicketInput, db: Session = Depends(database.get_db)):
    clean_desc = clean_text(ticket.description)
    
    # Predict Department
    pred_dept = dept_model.predict([clean_desc])[0] if dept_model else "General"
    
    # Predict Priority
    pred_prio = prio_model.predict([clean_desc])[0] if prio_model else "Low"

    # Database Save
    db_ticket = models.Ticket(
        description=ticket.description,
        predicted_dept=pred_dept,
        predicted_priority=pred_prio
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    
    return {
        "id": db_ticket.id,
        "description": ticket.description,
        "department": pred_dept,
        "priority": pred_prio
    }

# 6. Frontend Route (The Face)
@app.get("/")
def read_root():
    # Returns the HTML file when you visit http://localhost:8000
    return FileResponse(os.path.join(static_path, "index.html"))