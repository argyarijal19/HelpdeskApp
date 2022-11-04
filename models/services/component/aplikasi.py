from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

apps = Table(
    'aplikasi', meta,
    Column('id_aplikasi', Integer, primary_key=True),
    Column('nama_aplikasi', String(15)),
    Column('logo_aplikasi', String(20))
)
