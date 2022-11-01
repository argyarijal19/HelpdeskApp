from pydantic import BaseModel


class Role(BaseModel):
    id_role: int
    nama_role: str


class Update_role(BaseModel):
    nama_role: str
