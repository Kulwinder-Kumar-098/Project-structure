from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.user_controller import TaskController
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_controller(db: Session = Depends(get_db)) -> TaskController:
    return TaskController(db)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(controller: TaskController = Depends(get_controller)):
    """Return all tasks."""
    return controller.list_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, controller: TaskController = Depends(get_controller)):
    """Return a single task by ID."""
    return controller.get_task(task_id)


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(payload: TaskCreate, controller: TaskController = Depends(get_controller)):
    """Create a new task."""
    return controller.create_task(payload)


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    controller: TaskController = Depends(get_controller),
):
    """Partially update a task."""
    return controller.update_task(task_id, payload)


@router.delete("/{task_id}")
def delete_task(task_id: int, controller: TaskController = Depends(get_controller)):
    """Delete a task by ID."""
    return controller.delete_task(task_id)
