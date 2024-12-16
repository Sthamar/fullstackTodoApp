from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Date

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    deadline = Column(Date, nullable=False)
    completed = Column(Boolean, default=False)
    
    