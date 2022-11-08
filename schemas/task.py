from pydantic import BaseModel
from datetime import date


class Task(BaseModel):
    id_user_comp: int
    id_aplikasi: int
    id_jenis_task: int
    priority: int
    date_input: date


class Task_staff(BaseModel):
    id_user_staff: int
    date_done: date


class Task_rating(BaseModel):
    id_user_comp: int
    rating: int


class Done(BaseModel):
    status: int
