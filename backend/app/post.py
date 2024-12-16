from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session
from models import Task
from schemas import TaskOut, CreateTask
from database import get_db
from typing import List


router = APIRouter(prefix="/tasks", tags=['Tasks'])

@router.get("/", response_model=List[TaskOut])
def get_task(db:Session = Depends(get_db)):
    task = db.query(Task).all()
    return task

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=List[CreateTask])
def create_task(task: CreateTask, db:Session = Depends(get_db)):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return [new_task]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CreateTask)
def get_one_task(id:int, db:Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id: {id} not found")
    return task

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db:Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id)
    
    if task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id: {id} not found")
    task.delete(synchronize_session=False)
    db.commit()
    
@router.put("/tasks/{id}", response_model=CreateTask)
def update_task_content(update_task:CreateTask,id:int, db:Session=Depends(get_db)):
    updated_task = db.query(Task).filter(Task.id==id)
    
    if updated_task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_task.update(update_task.model_dump(),synchronize_session=False)
    db.commit()
    
    return updated_task.first()
    
    