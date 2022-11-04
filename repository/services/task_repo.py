from models.index import complain
from config.db import conn


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
