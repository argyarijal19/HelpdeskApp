from config.db import conn
from schemas.aplikasi import Apps
from models.index import apps
from fastapi.responses import FileResponse


def info_aplikasi():
    data = conn.execute(apps.select()).fetchall()
    return data


def info_aplikasi_byid(id_aplikasi: int):
    getID = apps.select().where(apps.c.id_aplikasi == id_aplikasi)
    data = conn.execute(getID).fetchall()
    return data


def inser_apps(app: Apps, filename: str):
    postData = conn.execute(apps.insert().values(
        id_aplikasi=app.id_aplikasi,
        nama_aplikasi=app.nama_aplikasi,
        logo_aplikasi=filename
    ))
    return postData
