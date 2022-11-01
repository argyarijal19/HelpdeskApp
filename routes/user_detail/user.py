from asyncio.windows_events import NULL
from logging import exception
from sqlalchemy.exc import IntegrityError, OperationalError
from fastapi import APIRouter
from schemas.user import User
from repository.user.user_repo import delete_user, post_data_user, put_data, staff, user_info, user_info_byid

user = APIRouter()


@user.get("/get_user", tags=["users_detail"])
async def get_user():
    data_user = user_info()
    if data_user:
        message = {'message': 'success',
                   'data': data_user, 'status': 0}
    else:
        message = {'message': 'Belum ada user yang ditemukan',
                   'data': NULL, 'status': 0}

    return message


@user.get("/getuser_byid/{id_user}", tags=["users_detail"])
async def get_user_byID(id_user: int):
    user_by_id = user_info_byid(id_user)
    if user_by_id:
        message = {'message': 'sucess',
                   'data': user_by_id, 'status': 0}
    else:
        message = {'message': f'user dengan id {id_user}',
                   'data': NULL, 'status': 0}

    return message


@user.get("/user_staff", tags=["users_detail"])
async def user_staff():
    data = staff()
    if data:
        message = {'message': 'sucess',
                   'data': data, 'status': 0}
    else:
        message = {'message': f'staff belum ada',
                   'data': NULL, 'status': 0}

    return message


@user.post("/post_user", tags=["users_detail"])
async def write_data(user: User):
    try:
        if '@gmail' in user.email or '@ulbi' in user.email:
            post_data_user(user)
            return {'message': 'Berhasil insert data', 'status': 1}
        else:
            return {'message': 'email harus menggunakan format @email atau @ulbi', 'status': 0}
    except IntegrityError:
        return {'message': 'GAGAL - Data jabatan atau role tidak sesuai', 'status': 0}
    except:
        return {'message': 'GAGAL - ada kesalahan saat menginputkan data', 'status': 0}


@user.put("/put_user/{id_user}", tags=["users_detail"])
async def update_data(id_user: int, user: User):
    putData = put_data(id_user, user)
    if putData == 1:
        message = {'message': 'Data berhasil di update', 'status': 1}
    else:
        message = {'message': 'Data gagal di update', 'status': 0}
    return message


@user.delete("/delete_user/{id_user}", tags=["users_detail"])
async def delete_data(id_user: int):
    delData = delete_user(id_user)
    if delData == 1:
        message = {'message': 'data berhasil di delete', 'status': 1}
    else:
        message = {'message': 'data gagal di delete', 'status': 0}
    return message
