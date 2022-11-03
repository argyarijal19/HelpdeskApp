from pydantic import BaseModel


class Jenis_task(BaseModel):
    id_aplikasi: int
    jenis_task: str
