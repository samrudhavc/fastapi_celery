# 🚀 FastAPI + Celery + Redis
A small application to test celery working with FastAPI

## Overview
This project demonstrates how to integrate **FastAPI**, **Celery**, and **Redis** for asynchronous task processing.
Redis acts as the message broker, Celery manages task execution, and FastAPI provides an API interface.

---

## 🛠 Setup Instructions

### 1️⃣ Prerequisites
Ensure the following are installed:
- **Python 3.9+**
- **Docker** (for Redis)
- **Git** (for version control)

### 2️⃣ Install Dependencies
Create a virtual environment and install required packages:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install fastapi uvicorn celery redis
