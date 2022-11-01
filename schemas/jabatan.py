from pydantic import BaseModel


class Jabatan(BaseModel):
    id_jabatan: int
    nama_jabatan: str


class Update_jabatan(BaseModel):
    nama_jabatan: str
