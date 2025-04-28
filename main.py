from fastapi import FastAPI
from celery.result import AsyncResult
from celery_app_mail import send_email
from celery_app_test import background_task

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

@app.post("/send-email/")
def send_email_task(subject: str, body: str, recipient: str):
    try:
        task = send_email.delay(subject, body, recipient)  # Asynchronously trigger the email task
        resp_data = {"task_id": task.id, "status": "Task submitted"}
    except Exception as ex:
        resp_data = {"message": ex, "status": "Not submitter"}
        print("Ex::",ex)
    return resp_data

@app.get("/email-status/{task_id}")
def get_email_status(task_id: str):
    result = AsyncResult(task_id)
    if result.state == "SUCCESS":
        return {"task_id": task_id, "status": result.state, "message": result.result}
    return {"task_id": task_id, "status": result.state}
