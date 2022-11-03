from config.db import conn
from models.index import jenis_task
from schemas.jenis_task import Jenis_task


def info_jtask() -> list:
    data = conn.execute(jenis_task.select()).fetchall()
    return data


def jtask_byid(id_jenis_task: int) -> list:
    getid = jenis_task.select().where(jenis_task.c.id_jenis_task == id_jenis_task)
    data = conn.execute(getid).fetchall()
    return data


def jtask_byapp(id_aplikasi: int) -> list:
    getid = jenis_task.select().where(jenis_task.c.id_aplikasi == id_aplikasi)
    data = conn.execute(getid).fetchall()
    return data


def post_jt(jt: Jenis_task):
    postData = conn.execute(jenis_task.insert().values(
        id_aplikasi=jt.id_aplikasi,
        jenis_task=jt.jenis_task
    ))
    return postData


def update_jt(jt: Jenis_task, id_jenis_task: int) -> int:
    putData = conn.execute(jenis_task.update().values(
        jenis_task=jt.jenis_task,
        id_aplikasi=jt.id_aplikasi
    ).where(jenis_task.c.id_jenis_task == id_jenis_task))
    return putData.rowcount


def delete_jt(id_jenis_task: int) -> int:
    delete = conn.execute(jenis_task.delete().where(
        jenis_task.c.id_jenis_task == id_jenis_task))
    return delete.rowcount
