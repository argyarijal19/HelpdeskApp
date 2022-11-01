from dataclasses import Field
from tkinter import HIDDEN
from turtle import hideturtle
from pydantic import BaseModel, SecretStr


class User(BaseModel):
    # id_user: int
    id_jabatan: int
    id_role: int
    nama_lengkap: str
    email: str
    password: str
