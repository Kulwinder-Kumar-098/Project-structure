from sqlalchemy.orm import Session

from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate


class TaskService:
    def __init__(self, db: Session):
        self.repo = TaskRepository(db)

    def get_all_tasks(self) -> list[TaskResponse]:
        tasks = self.repo.get_all()
        return [TaskResponse.model_validate(t) for t in tasks]

    def get_task(self, task_id: int) -> TaskResponse | None:
        task = self.repo.get_by_id(task_id)
        if not task:
            return None
        return TaskResponse.model_validate(task)

    def create_task(self, payload: TaskCreate) -> TaskResponse:
        task = self.repo.create(payload)
        return TaskResponse.model_validate(task)

    def update_task(self, task_id: int, payload: TaskUpdate) -> TaskResponse | None:
        task = self.repo.update(task_id, payload)
        if not task:
            return None
        return TaskResponse.model_validate(task)

    def delete_task(self, task_id: int) -> bool:
        return self.repo.delete(task_id)
