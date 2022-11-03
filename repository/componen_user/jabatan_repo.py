from config.db import conn
from models.index import jobs
from schemas.jabatan import Jabatan, Update_jabatan


def jabatan_all() -> list:
    data = conn.execute(jobs.select()).fetchall()
    return data


def jabatan_byid(id_jabatan: int) -> list:
    getJabatan = jobs.select().where(jobs.c.id_jabatan == id_jabatan)
    data = conn.execute(getJabatan).fetchall()
    return data


def insert_jabatan(jabatan: Jabatan):
    postData = conn.execute(jobs.insert().values(
        id_jabatan=jabatan.id_jabatan,
        nama_jabatan=jabatan.nama_jabatan
    ))
    return postData


def update_jabatan(id_jabatan: int, jabatan: Update_jabatan) -> int:
    putData = conn.execute(jobs.update().values(
        nama_jabatan=jabatan.nama_jabatan,
    ).where(jobs.c.id_jabatan == id_jabatan))
    return putData.rowcount


def del_jabatan(id_jabatan: int) -> int:
    delete = conn.execute(jobs.delete().where(jobs.c.id_jabatan == id_jabatan))
    return delete.rowcount
