from asyncio.windows_events import NULL
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter
from repository.componen_user.role_repo import all_role, role_insert, role_byid
from schemas.role import Role, Update_role

role = APIRouter()


@role.get("/all_role", tags=["Role_detail"])
async def getRole():
    data = all_role()
    if data:
        message = {'message': 'success',
                   'data': data, 'status': 1}
    else:
        message = {'message': 'Belum ada user yang ditemukan',
                   'data': NULL, 'status': 0}
    return message


@role.get("/get_role_byid/{id_role}", tags=["Role_detail"])
async def get_role_byID(id_role: int):
    data = role_byid(id_role)
    if data:
        message = {'message': 'success',
                   'data': data, 'status': 1}
    else:
        message = {'message': f'user dengan id {id_role}',
                   'data': NULL, 'status': 0}

    return message


@role.post("/post_role", tags=["Role_detail"])
async def post_role(role: Role):
    try:
        role_insert(role)
        message = {'message': 'Success insert data', 'status': 1}
    except IntegrityError:
        message = {
            'message': 'Gagal Input data, ID dan nama role Role tidak boleh duplikat', 'status': 0}

    return message


@role.put("/update_role/{id_role}", tags=["Role_detail"])
async def update_role(id_role: int, roles: Update_role):
    update = update_role(id_role, roles)
    if update == 1:
        message = {'message': 'data berhasil di delete', 'status': 1}
    else:
        message = {
            'message': 'data gagal di update - ID tidak ditemukan', 'status': 0}
    return message
