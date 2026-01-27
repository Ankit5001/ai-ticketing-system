from pydantic import BaseModel

class TicketInput(BaseModel):
    description: str

class TicketOutput(BaseModel):
    id: int
    description: str
    department: str
    priority: str = "Medium" # Default for now
    
    class Config:
        from_attributes = True