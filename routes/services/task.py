from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError
from asyncio.windows_events import NULL
from repository.services.task_repo import *
from schemas.task import *
from repository.user.user_repo import staff
from repository.user.user_repo import staff, user_info_byid


task = APIRouter()


@task.get("/all_task_ws", tags=["Services"])
async def get_data():
    data = all_task_with_staff()
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': 'task tidak ada',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_ns", tags=["Services"])
async def get_task_no_staff():
    data = all_task_no_staff()
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': 'task tidak ada',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_ws_byid", tags=["Services"])
async def get_task_with_staff_byid(id_task: int):
    data = all_task_with_staff_byid(id_task)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task yang sedang ditangani atau sudah selesai dengan id {id_task}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_ns_byid", tags=["Services"])
async def get_task_no_staff_byid(id_task: int):
    data = all_task_no_staff_byid(id_task)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task yang belum ditangani dengan id {id_task}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_bystaff", tags=["Services"])
async def get_task_bystaff(id_staff: int):
    data = all_task_bystaff(id_staff)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task dengan id staff {id_staff}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_byuser_ns", tags=["Services"])
async def get_task_byuser_ns(id_user: int):
    data = all_task_byuser_and_ns(id_user)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task yang belum ditangani dengan id {id_user}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_byuser_ws", tags=["Services"])
async def get_task_byuser_ws(id_user: int):
    data = all_task_byuser_ws(id_user)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task yang sedang ditangani atau sudah selesai dengan id {id_user}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_byuser_tsdone", tags=["Services"])
async def get_task_byuser_tsdone(id_user: int):
    data = all_task_byuser_done(id_user)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task yang sudah selesai dengan id_user {id_user}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/all_task_bystaff_done", tags=["Services"])
async def get_task_bystaff_done(id_staff: int):
    data = all_task_bystaff_done(id_staff)
    if data:
        message = {'message': 'success get data',
                   'data': data,  'status': 1}
    else:
        message = {'message': f'tidak ada task yang sudah selesai dengan id_staff {id_staff}',
                   'data': NULL, 'status': 0}
    return message


@task.get("/get_staff_rate", tags=["Services"])
async def get_rating_for_staff(id_staff: int):
    rate_data = get_rating_staff(id_staff)
    data_staff = staff(20)
    id_user_staff = []
    for data in data_staff:
        id_user_staff.append(data["id_user"])
    if id_staff in id_user_staff:
        if rate_data:
            return rate_data
        else:
            return {'rating': 0}
    else:
        return {'message': 'id bukan terdaftar sebagai staff'}


@task.put("/update_staff_dl/{id_task}", tags=["Services"])
async def put_staff_dl(task: Task_staff, id_task: int):
    data_staff = staff(20)
    id_staff = []
    for item in data_staff:
        id_staff.append(item["id_user"])
    if task.id_user_staff in id_staff:
        update = update_task_staff_dl(task, id_task)
        if update == 1:
            message = {'message': 'sucess update data', 'status': 1}
        else:
            message = {
                'message': 'GAGAL - something went wrong', 'status': 0}
    else:
        message = {
            'message': 'GAGAL - id_staff tidak sesuai', 'status': 0}
    return message


@task.put("/update_task_rating", tags=["Services"])
async def put_rating(task: Task_rating, id_task: int):
    data_task = all_task_with_staff_byid(id_task)
    if task.id_user_comp == data_task[0]["id_user_comp"]:
        update = update_task_rating(task, id_task)
        if update == 1:
            message = {'message': 'update data successs', 'status': 1}
        else:
            message = {
                'message': 'update data gagal - id_user tidak sesuai', 'status': 0}
    else:
        message = {
            'message': 'update data gagal - ini bukan task yang anda masukan', 'status': 0}

    return message


@task.delete("/delete_task/{id_task}", tags=['Services'])
async def del_task(id_task: int):
    delete = delete_task(id_task)
    if delete == 1:
        message = {'message': 'delete data successs', 'status': 1}
    else:
        message = {
            'message': 'delete data gagal - id_user tidak sesuai', 'status': 0}

    return message
