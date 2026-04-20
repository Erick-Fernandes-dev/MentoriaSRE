from fastapi import FastAPI, Depends, HTTPException
from typing import List


from .domain import Task, TaskCreate
from .use_cases import TaskService
from .dependencies import get_task_service

app = FastAPI(title="Clean API Kubernetes")

@app.get("/")
def health_check():
    return {"status": "Runing", "architecture": "Clean Code"}

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(
        task: TaskCreate,
        service: TaskService = Depends(get_task_service)
):
    try:
        return service.create_task(task)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks", response_model=List[Task])
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.list_tasks()






