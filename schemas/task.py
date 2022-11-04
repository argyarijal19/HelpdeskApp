from pydantic import BaseModel
from datetime import date
from schemas.status import Status


class Task(BaseModel):
    id_user_comp: int
    id_user_staff: int
    id_aplikasi: int
    id_jenis_task: int
    status: Status
    priority: int
    rating: int
    date_input: date
    date_done: date


class Task_staff(BaseModel):
    id_user_staff: int
    date_done: date
