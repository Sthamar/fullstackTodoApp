from pydantic import BaseModel, field_validator
from datetime import date

class CreateTask(BaseModel):
    title:str
    description: str
    created_at:date = date.today()
    deadline: date
    completed:bool = False
    @field_validator('deadline')
    def check_deadline(cls, value):
        if value <= date.today():
            raise ValueError("Deadline must be in the future.")
        return value
    
    class Config:
        from_attributes = True
        
class TaskOut(BaseModel):
    id:int
    title:str
    description: str
    created_at: date
    deadline: date
    completed:bool
    
    class Config:
        from_attributes = True
    
    