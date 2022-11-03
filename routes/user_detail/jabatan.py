from asyncio.windows_events import NULL
from sqlalchemy.exc import IntegrityError, OperationalError
from fastapi import APIRouter
from repository.componen_user.jabatan_repo import *
from schemas.jabatan import Jabatan, Update_jabatan

job = APIRouter()


@job.get("/jabatan", tags=["jabatan_detail"])
async def get_jabatan():
    data = jabatan_all()
    if data:
        message = {'message': 'success',
                   'data': data, 'status': 1}
    else:
        message = {'message': 'Belum ada user yang ditemukan',
                   'data': NULL, 'status': 0}

    return message


@job.get("/id_jabatan/{id_jabatan}", tags=["jabatan_detail"])
async def get_job_byID(id_jabatan: int):
    data = jabatan_byid(id_jabatan)
    if data:
        message = {'message': 'success',
                   'data': data, 'status': 1}
    else:
        message = {'message': f'user dengan id {id_jabatan}',
                   'data': NULL, 'status': 0}

    return message


@job.post("/post_jabatan", tags=["jabatan_detail"])
async def post_jabatan(jabatan: Jabatan):
    try:
        insert_jabatan(jabatan)
        return {'message': 'Berhasil insert data', 'status': 1}
    except IntegrityError:
        return {'message': 'GAGAL- tidak boleh ada data duplicate', 'status': 0}


@job.put("/update_jabatan", tags=["jabatan_detail"])
async def update(id_jabatan: int, jabatan: Update_jabatan):
    putData = update_jabatan(id_jabatan, jabatan)
    if putData == 1:
        message = {'message': 'Data berhasil di update', 'status': 1}
    else:
        message = {
            'message': 'Data gagal di update - ID tidak ditemukan', 'status': 0}
    return message


@job.delete("/delete_job", tags=["jabatan_detail"])
async def job_delete(id_jabatan: int):
    try:
        delData = del_jabatan(id_jabatan)
        if delData == 1:
            message = {'message': 'data berhasil di delete', 'status': 1}
        else:
            message = {
                'message': 'data gagal di delete - ID tidak ditemukan', 'status': 0}
        return message
    except IntegrityError:
        return {'message': 'foreign key constraint fails - Data tidak bisa di delete', 'status': 0}
