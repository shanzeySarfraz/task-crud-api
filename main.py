from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from repository.postgres_repository import PostgresTaskRepository


app = FastAPI(title="Task API")

repository = PostgresTaskRepository()


class Task(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "3.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return repository.get_all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = repository.get_by_id(task_id)

    if task:
        return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    if task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title is required")

    return repository.create(task.title, task.done)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: Task):
    if updated.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title is required")

    task = repository.update(task_id, updated.title, updated.done)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = repository.delete(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return None
