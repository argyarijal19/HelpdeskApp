from fastapi import APIRouter
from asyncio.windows_events import NULL
from sqlalchemy.exc import IntegrityError
from schemas.jenis_task import Jenis_task
from repository.services.component.jenis_task_repo import *


jt = APIRouter()


@jt.get("/jenis_task", tags=["jenis_task detail"])
async def get_jt():
    data = info_jtask()
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': 'belum ada task yang tersedia',
                   'data': NULL, 'status': 0}
    return message


@jt.get("/jt_byid", tags=["jenis_task detail"])
async def get_jt_byid(id_jenis_task: int):
    data = jtask_byid(id_jenis_task)
    if data:
        message = {'message': 'success get data', 'data': data, 'status': 1}
    else:
        message = {'message': f'aplikasi tidak ditemukan dengan id {id_jenis_task}',
                   'data': NULL, 'status': 0}
    return message


@jt.get("/jt_byapp", tags=["jenis_task detail"])
async def get_jt_byapp(id_aplikasi: int):
    data = jtask_byapp(id_aplikasi)
    if data:
        message = {'message': 'success get data', 'data': data, 'status': 1}
    else:
        message = {'message': f'aplikasi tidak ditemukan dengan id {id_aplikasi}',
                   'data': NULL, 'status': 0}
    return message


@jt.post("/post_jt", tags=["jenis_task detail"])
async def post_data(jt: Jenis_task):
    try:
        post_jt(jt)
        return {'message': 'Berhasil insert data', 'status': 1}
    except IntegrityError:
        return {'message': 'GAGAL- id_aplikasi tidak sesuai', 'status': 0}


@jt.put("/update_jt", tags=["jenis_task detail"])
async def put_jt(jt: Jenis_task, id_jenis_task: int):
    try:
        putData = update_jt(jt, id_jenis_task)
        if putData == 1:
            message = {'message': 'Data berhasil di update', 'status': 1}
        else:
            message = {
                'message': 'Data gagal di update - ID tidak ditemukan', 'status': 0}
    except IntegrityError:
        message = {
            'message': 'Data gagal di update - ID_aplikasi tidak sesuai', 'status': 0}
    return message


@jt.delete("/delete_jt", tags=["jenis_task detail"])
async def del_data(id_jenis_task: int):
    try:
        delData = delete_jt(id_jenis_task)
        if delData == 1:
            message = {'message': 'data berhasil di delete', 'status': 1}
        else:
            message = {
                'message': 'data gagal di delete - ID tidak ditemukan', 'status': 0}
        return message
    except IntegrityError:
        return {'message': 'foreign key constraint fails - Data tidak bisa di delete', 'status': 0}
