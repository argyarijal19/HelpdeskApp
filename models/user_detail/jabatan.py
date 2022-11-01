from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

jobs = Table(
    'jabatan', meta,
    Column('id_jabatan', Integer, primary_key=True),
    Column('nama_jabatan', String(30))
)
