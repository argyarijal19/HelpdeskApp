from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, VARCHAR
from config.db import meta

role = Table(
    'role', meta,
    Column('id_role', Integer, primary_key=True),
    Column('nama_role', String(40)),
)
