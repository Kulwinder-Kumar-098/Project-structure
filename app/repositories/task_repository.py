from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Task]:
        return self.db.query(Task).all()

    def get_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create(self, payload: TaskCreate) -> Task:
        task = Task(
            title=payload.task,
            description=payload.description or "",
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, task_id: int, payload: TaskUpdate) -> Task | None:
        task = self.get_by_id(task_id)
        if not task:
            return None
        if payload.task is not None:
            task.title = payload.task
        if payload.description is not None:
            task.description = payload.description
        if payload.completed is not None:
            task.completed = payload.completed
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if not task:
            return False
        self.db.delete(task)
        self.db.commit()
        return True
