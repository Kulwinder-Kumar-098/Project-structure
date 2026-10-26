from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.user_service import TaskService


class TaskController:
    def __init__(self, db: Session):
        self.service = TaskService(db)

    def list_tasks(self) -> list[TaskResponse]:
        return self.service.get_all_tasks()

    def get_task(self, task_id: int) -> TaskResponse:
        task = self.service.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def create_task(self, payload: TaskCreate) -> TaskResponse:
        return self.service.create_task(payload)

    def update_task(self, task_id: int, payload: TaskUpdate) -> TaskResponse:
        task = self.service.update_task(task_id, payload)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def delete_task(self, task_id: int) -> dict:
        deleted = self.service.delete_task(task_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully"}
