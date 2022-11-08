from sqlalchemy import Table, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, Enum
from models.index import users, apps, jenis_task
from config.db import meta
import datetime


complain = Table(
    'task', meta,
    Column('id_task', Integer, primary_key=True),
    Column('id_user_comp', Integer, ForeignKey(users.c.id_user)),
    Column('id_user_staff', Integer, ForeignKey(users.c.id_user)),
    Column('id_aplikasi', Integer, ForeignKey(apps.c.id_aplikasi)),
    Column('id_jenis_task', Integer, ForeignKey(jenis_task.c.id_jenis_task)),
    Column('status', Enum),
    Column('priority', Integer),
    Column('rating', Integer),
    Column('date_input', DateTime, default=datetime.datetime.utcnow),
    Column('date_done', DateTime)
)
