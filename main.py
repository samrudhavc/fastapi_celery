from fastapi import FastAPI
from celery.result import AsyncResult
from celery_app import background_task

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with Celery!"}

@app.post("/run-task/{x}/{y}")
async def run_task(x: int, y: int):
    task = background_task.delay(x, y)
    return {"task_id": task.id, "status": "processing"}

@app.get("/task-status/{task_id}")
async def task_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status, "result": task_result.result}