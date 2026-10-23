from pydantic import BaseModel, ConfigDict,  Field

class TaskCreate(BaseModel):
    task: str=Field(default=1, max_length=100)
    description: str=Field(default=None,max_length=1000)
class TaskUpdate(BaseModel):
    task: str | None =Field(default=None, max_length=100)
    description: str | None =Field(default=None, max_length=1000)
    completed: bool | None = None
class TaskResponse(BaseModel):
    model_config =ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    completed: bool