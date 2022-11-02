import os
from typing import Optional
from asyncio.windows_events import NULL
from sqlalchemy.exc import IntegrityError
from repository.services.component.applikasi_repo import del_apps, info_aplikasi, info_aplikasi_byid, inser_apps, update_apps, update_apps_noIm
from fastapi import APIRouter, File, UploadFile, Depends
from schemas.aplikasi import Apps, Apps_update

apps = APIRouter()


@apps.get("/get_apps", tags=["apps_detail"])
async def get_apps():
    data = info_aplikasi()
    if data:
        # for filename in data[2]:
        #     im = Image.open(f'logoaplikasi/{filename}')
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': 'aplikasi tidak ditemukan',
                   'data': NULL, 'status': 0}
    return message


@apps.get("/get_appsID/{id_aplikasi}", tags=["apps_detail"])
async def get_id_apps(id_aplikasi: int):
    data = info_aplikasi_byid(id_aplikasi)
    if data:
        message = {'message': 'success get data', 'data': data, 'status': 1}
    else:
        message = {'message': f'aplikasi tidak ditemukan dengan id {id_aplikasi}',
                   'data': NULL, 'status': 0}
    return message


@apps.post("/post_app", tags=["apps_detail"])
async def post_apps(logo: UploadFile = File(...), app: Apps = Depends()):
    try:
        file_name = f'logoaplikasi/{app.id_aplikasi}.png'
        with open(file_name, 'wb') as buffer:
            buffer.write(logo.file.read())
        # data_db = app.dict()
        inser_apps(app, file_name)
        return {'message': 'Berhasil insert data', 'status': 1}
    except IntegrityError:
        return {'message': 'GAGAL- tidak boleh ada data duplicate', 'status': 0}


@apps.put("/update_aplikasi/{id_aplikasi}", tags=["apps_detail"])
async def update_aplikasi(id_aplikasi: int, app: Apps_update = Depends(), logo: UploadFile = File(None)):
    try:
        if logo:
            file_name = f'logoaplikasi/{id_aplikasi}.png'
            if os.path.exists(file_name):
                os.remove(file_name)
                with open(file_name, 'wb') as buffer:
                    buffer.write(logo.file.read())
                update = update_apps(app, id_aplikasi, file_name)
                if update == 1:
                    message = {'message': 'berhasil Update data!', 'status': 1}
                else:
                    message = {'message': 'Gagal Update Data', 'status': 0}
        else:
            update = update_apps_noIm(app, id_aplikasi)
            if update == 1:
                message = {'message': 'berhasil Update data!', 'status': 1}
            else:
                message = {'message': 'Gagal Update Data', 'status': 0}
        return message
    except:
        pass


@apps.delete("/deleteApp/{id_aplikasi}", tags=["apps_detail"])
async def delete_apps(id_aplikasi: int):
    if os.path.exists(f'logoaplikasi/{id_aplikasi}.png'):
        delete = del_apps(id_aplikasi)
        os.remove(f'logoaplikasi/{id_aplikasi}.png')
        if delete == 1:
            message = {
                'message': 'data berhasil di delete dan file berhasil di hapus', 'status': 1}
        else:
            message = {
                'message': 'data gagal di delete tapi file berhasil di hapus', 'status': 0}
    else:
        delete = del_apps(id_aplikasi)
        if delete == 1:
            message = {
                'message': 'data berhasil di delete file tidak ada', 'status': 1}
        else:
            message = {
                'message': 'data gagal di delete tapi file tidak ada', 'status': 0}
    return message
