from pydantic import BaseModel


class Apps(BaseModel):
    id_aplikasi: int
    nama_aplikasi: str
    # logo_aplikasi: str


class Apps_update(BaseModel):
    nama_aplikasi: str
