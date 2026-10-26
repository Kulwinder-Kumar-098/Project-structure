# Task Manager

A full-stack **Task Manager** built with:

- **Backend** – FastAPI + SQLAlchemy + SQLite
- **Frontend** – Streamlit

## Project Structure

```
project_structure/
├── app/
│   ├── api/v1/endpoints/users.py   ← REST endpoints
│   ├── controllers/user_controller.py
│   ├── core/config.py
│   ├── db/{base,session}.py
│   ├── models/task.py              ← SQLAlchemy ORM model
│   ├── repositories/task_repository.py
│   ├── schemas/task.py             ← Pydantic schemas
│   ├── services/user_service.py
│   └── main.py                     ← FastAPI app entry point
├── streamlit_app.py                ← Streamlit frontend
├── requirements.txt
├── pyproject.toml
└── .env
```

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI backend
```bash
uvicorn app.main:app --reload
```
API is available at http://127.0.0.1:8000  
Interactive docs at http://127.0.0.1:8000/docs

### 3. Start the Streamlit frontend (new terminal)
```bash
streamlit run streamlit_app.py
```
UI is available at http://localhost:8501

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/tasks/` | List all tasks |
| GET | `/api/v1/tasks/{id}` | Get task by ID |
| POST | `/api/v1/tasks/` | Create task |
| PATCH | `/api/v1/tasks/{id}` | Update task |
| DELETE | `/api/v1/tasks/{id}` | Delete task |
