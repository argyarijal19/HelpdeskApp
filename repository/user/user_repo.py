from config.db import conn
from sqlalchemy.orm import session
from cryptography.fernet import Fernet
from schemas.user import User
from models.index import users


def user_info() -> list:
    query = "SELECT users.id_user, users.id_jabatan, jabatan.nama_jabatan as jabatan, users.id_role, role.nama_role as role, users.nama_lengkap, users.email, users.password FROM users JOIN jabatan ON users.id_jabatan=jabatan.id_jabatan JOIN role ON role.id_role=users.id_role"
    data = conn.execute(query).fetchall()
    return data


def staff(id_role: int) -> list:
    query = f'SELECT users.id_user, users.id_jabatan, jabatan.nama_jabatan as jabatan, users.id_role, role.nama_role as role, users.nama_lengkap, users.email, users.password FROM users JOIN jabatan ON users.id_jabatan=jabatan.id_jabatan JOIN role ON role.id_role=users.id_role WHERE role.id_role = {id_role}'
    data = conn.execute(query).fetchall()
    return data


def user_info_byid(id_user: int) -> list:
    query = f"SELECT  users.id_user, users.id_jabatan, jabatan.nama_jabatan as jabatan, users.id_role, role.nama_role as role, users.nama_lengkap, users.email, users.password FROM users JOIN jabatan ON users.id_jabatan=jabatan.id_jabatan JOIN role ON role.id_role=users.id_role WHERE id_user = {id_user}"
    data = conn.execute(query).fetchall()
    return data


def total_row() -> int:
    query = "SELECT COUNT(id_user) FROM users"
    maxrow = conn.execute(query).fetchone()[0] + 1
    return maxrow


def post_data_user(user: User):
    id_user = int('{}{}{}'.format(user.id_jabatan, user.id_role, total_row()))
    # encryp data using fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(user.password.encode())
    postData = conn.execute(users.insert().values(
        id_user=id_user,
        id_jabatan=user.id_jabatan,
        id_role=user.id_role,
        nama_lengkap=user.nama_lengkap,
        email=user.email,
        password=encMessage
    ))
    return postData


def put_data(id_user: int, user: User) -> int:
    putData = conn.execute(users.update().values(
        id_jabatan=user.id_jabatan,
        id_role=user.id_role,
        nama_lengkap=user.nama_lengkap,
        email=user.email,
        password=user.password
    ).where(users.c.id_user == id_user))
    return putData.rowcount


def delete_user(id_user: int) -> int:
    delete = conn.execute(users.delete().where(users.c.id_user == id_user))
    return delete.rowcount
