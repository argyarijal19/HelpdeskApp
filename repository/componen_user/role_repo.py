from config.db import conn
from models.index import role
from schemas.role import Role, Update_role


def all_role():
    data = conn.execute(role.select()).fetchall()
    return data


def role_byid(id_role: int):
    data_role = role.select().where(role.c.id_role == id_role)
    data = conn.execute(data_role).fetchall()
    return data


def role_insert(roles: Role):
    postData = conn.execute(role.insert().values(
        id_role=roles.id_role,
        nama_role=roles.nama_role
    ))
    return postData


def role_update(id_role, roles: Update_role):
    updateData = conn.execute(role.update(). values(
        nama_role=roles.nama_role
    ))
    return updateData.rowcount
