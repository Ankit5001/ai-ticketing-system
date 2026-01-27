from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    predicted_dept = Column(String)
    predicted_priority = Column(String) # If you add priority prediction logic
    created_at = Column(DateTime, default=datetime.utcnow)