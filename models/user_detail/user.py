from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, VARCHAR
from config.db import meta
from models.user_detail.jabatan import jobs

users = Table(
    'users', meta,
    Column('id_user', Integer, primary_key=True),
    Column('id_jabatan', Integer, ForeignKey(jobs.c.id_jabatan)),
    Column('id_role', Integer),
    Column('nama_lengkap', String(40)),
    Column('email', VARCHAR(60), unique=True, index=True),
    Column('password', VARCHAR(350))
)
