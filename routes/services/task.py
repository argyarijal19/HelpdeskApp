from fastapi import APIRouter
from asyncio.windows_events import NULL
from repository.services.task_repo import *


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
