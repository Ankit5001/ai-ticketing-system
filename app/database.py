from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------
# UPDATE THIS LINE
# format: postgresql://USER:PASSWORD@HOST/DATABASE_NAME
# ---------------------------------------------------------
# Replace '1234' with the REAL password you typed in the SQL Shell
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ankit800@localhost/ticket_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()