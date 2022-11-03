from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta
from models.services.component.aplikasi import apps

jenis_task = Table(
    'jenis_task', meta,
    Column('id_jenis_task', Integer, primary_key=True),
    Column('id_aplikasi', Integer, ForeignKey(apps.c.id_aplikasi)),
    Column('jenis_task', String(15))
)
