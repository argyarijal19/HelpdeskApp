from models.index import complain
from config.db import conn
from schemas.task import *
from repository.user.user_repo import user_info_byid


def get_rating_staff(id_staff: int) -> list:
    query = f"SELECT AVG(rating) AS rating FROM task WHERE id_user_staff = {id_staff} GROUP BY id_user_staff;"
    data = conn.execute(query).fetchall()
    return data


def get_all_rating_staff() -> list:
    query = f"SELECT AVG(t.rating) AS rating, u.nama_lengkap, COUNT(t.rating) as jumlah_task FROM task t JOIN users u ON t.id_user_staff=u.id_user GROUP BY id_user_staff;"
    data = conn.execute(query).fetchall()
    return data


def all_task_no_staff() -> list:
    query = "SELECT ts.id_user_comp, ts.id_user_staff,  us.id_jabatan, jt.id_jenis_task, jt.jenis_task, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain,  ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi JOIN jenis_task jt ON jt.id_jenis_task=ts.id_jenis_task WHERE ts.id_user_staff is null ORDER BY ts.priority DESC"
    data = conn.execute(query).fetchall()
    return data


def all_task_with_staff() -> list:
    query = "SELECT ts.id_user_comp, ts.id_user_staff,  up.id_jabatan, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain, up.nama_lengkap as user_staff, ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN users up ON up.id_user=ts.id_user_staff JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi"
    data = conn.execute(query).fetchall()
    return data


def all_task_no_staff_byid(id_task: int) -> list:
    query = f'SELECT ts.id_user_comp, ts.id_user_staff,  us.id_jabatan, jt.id_jenis_task, jt.jenis_task, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain,  ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi JOIN jenis_task jt ON jt.id_jenis_task=ts.id_jenis_task WHERE ts.id_user_staff is null AND ts.id_task = {id_task} ORDER BY ts.priority DESC'
    data = conn.execute(query).fetchall()
    return data


def all_task_with_staff_byid(id_task: int) -> list:
    query = f'SELECT ts.id_user_comp, ts.id_user_staff,  up.id_jabatan, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain, up.nama_lengkap as user_staff, ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN users up ON up.id_user=ts.id_user_staff JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi WHERE ts.id_task = {id_task}'
    data = conn.execute(query).fetchall()
    return data


def all_task_bystaff(id_staff: int) -> list:
    query = f'SELECT ts.id_user_comp, ts.id_user_staff,  up.id_jabatan, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain, up.nama_lengkap as user_staff, ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN users up ON up.id_user=ts.id_user_staff JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi WHERE ts.id_user_staff = {id_staff}'
    data = conn.execute(query).fetchall()
    return data


def all_task_byuser_and_ns(id_user: int) -> list:
    query = f'SELECT ts.id_user_comp, ts.id_user_staff,  us.id_jabatan, jt.id_jenis_task, jt.jenis_task, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain,  ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi JOIN jenis_task jt ON jt.id_jenis_task=ts.id_jenis_task WHERE ts.id_user_staff is null AND ts.id_user_comp = {id_user}'
    data = conn.execute(query).fetchall()
    return data


def all_task_byuser_ws(id_user: int) -> list:
    query = f'SELECT ts.id_user_comp, ts.id_user_staff,  up.id_jabatan, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain, up.nama_lengkap as user_staff, ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN users up ON up.id_user=ts.id_user_staff JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi WHERE ts.id_user_comp = {id_user}'
    data = conn.execute(query).fetchall()
    return data


def all_task_byuser_done(id_user: int) -> list:
    query = f"SELECT ts.id_user_comp, ts.id_user_staff,  up.id_jabatan, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain, up.nama_lengkap as user_staff, ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN users up ON up.id_user=ts.id_user_staff JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi WHERE ts.id_user_comp = {id_user} AND ts.status = '2'"
    data = conn.execute(query).fetchall()
    return data


def all_task_bystaff_done(id_staff: int) -> list:
    query = f"SELECT ts.id_user_comp, ts.id_user_staff,  up.id_jabatan, ts.id_aplikasi,ap.nama_aplikasi, ap.logo_aplikasi, us.nama_lengkap as user_complain, up.nama_lengkap as user_staff, ts.status, ts.priority, ts.rating, ts.date_input, ts.date_done FROM users us JOIN task ts ON us.id_user=ts.id_user_comp JOIN users up ON up.id_user=ts.id_user_staff JOIN aplikasi ap ON ap.id_aplikasi=ts.id_aplikasi WHERE ts.id_user_staff = {id_staff} AND ts.status = '2'"
    data = conn.execute(query).fetchall()
    return data


def update_task_staff_dl(task: Task_staff, id_task: int) -> int:
    putData = conn.execute(complain.update().values(
        id_user_staff=task.id_user_staff,
        status='1',
        date_done=task.date_done
    ).where(complain.c.id_task == id_task))
    return putData.rowcount


def update_task_rating(task: Task_rating, id_task: int) -> int:
    putData = conn.execute(complain.update().values(
        id_user_comp=task.id_user_comp,
        status='2',
        rating=task.rating
    ).where(complain.c.id_task == id_task))
    return putData.rowcount


def post_task(task: Task):
    id_jabatan = user_info_byid(task.id_user_comp)
    aplikasi = task.id_aplikasi
    priority = (id_jabatan[0]["id_jabatan"] + aplikasi) / 2
    postData = conn.execute(complain.insert().values(
        id_user_comp=task.id_user_comp,
        id_aplikasi=task.id_aplikasi,
        id_jenis_task=task.id_jenis_task,
        priority=priority
    ))
    return postData


def delete_task(id_task: int) -> int:
    delete = conn.execute(complain.delete().where(
        complain.c.id_task == id_task))
    return delete.rowcount
