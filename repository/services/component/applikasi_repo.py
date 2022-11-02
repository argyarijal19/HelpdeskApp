from config.db import conn
from schemas.aplikasi import Apps, Apps_update
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


def update_apps(app: Apps_update, id_aplikasi: int, filename: str):
    putData = conn.execute(app.update().values(
        id_aplikasi=app.id_aplikasi,
        nama_aplikasi=app.nama_aplikasi,
        logo_aplikasi=filename
    ).where(app.c.id_aplikasi == id_aplikasi))
    return putData.rowcount


def del_apps(id_aplikasi: int):
    delete = conn.execute(apps.delete().where(
        apps.c.id_aplikasi == id_aplikasi))
    return delete.rowcount
