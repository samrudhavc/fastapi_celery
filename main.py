from fastapi import FastAPI
from celery.result import AsyncResult
from celery_app_mail import send_email
from celery_app_test import background_task
from models import EmailRequest  # Import the model
from settings import settings

# app = FastAPI()
app = FastAPI(title=settings.APP_NAME)  # Use the app name from settings.py

@app.get("/config")
async def get_config():
    return {
        "database_url": settings.DATABASE_URL,
        "smtp_server": settings.SMTP_SERVER,
        "celery_broker": settings.CELERY_BROKER_URL,
    }

# from sqlalchemy import create_engine
# DATABASE_URL = f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
# engine = create_engine(DATABASE_URL)

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
def send_email_task(request: EmailRequest):  # Use EmailRequest model for validation
    try:
        task = send_email.delay(request.subject, request.body, request.recipient)  # Trigger Celery task
        resp_data = {"task_id": task.id, "status": "Task submitted"}
    except Exception as ex:
        resp_data = {"message": str(ex), "status": "Not submitted"}  # Convert exception to string for response
        print("Exception:", ex)
    return resp_data

@app.get("/email-status/{task_id}")
def get_email_status(task_id: str):
    result = AsyncResult(task_id)
    if result.state == "SUCCESS":
        return {"task_id": task_id, "status": result.state, "message": result.result}
    return {"task_id": task_id, "status": result.state}
