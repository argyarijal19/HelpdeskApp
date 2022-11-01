import os
import shutil
from PIL import Image
from asyncio.windows_events import NULL
from sqlalchemy.exc import IntegrityError
from repository.services.applikasi_repo import info_aplikasi, info_aplikasi_byid, inser_apps
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import FileResponse
from schemas.aplikasi import Apps

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
async def post_jabatan(logo: UploadFile = File(...), app: Apps = Depends()):
    try:
        file_name = f'{app.id_aplikasi}.png'
        with open(f'logoaplikasi/{app.nama_aplikasi}.png', 'wb') as buffer:
            buffer.write(logo.file.read())
        # data_db = app.dict()
        inser_apps(app, file_name)
        return {'message': 'Berhasil insert data', 'status': 1}
    except IntegrityError:
        return {'message': 'GAGAL- tidak boleh ada data duplicate', 'status': 0}
