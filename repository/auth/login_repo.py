from config.db import conn
from models.index import users
from schemas.login import UserLoginSchema


# ini query untuk login username dan password
def get_email(email: str) -> dict:
    getdata = f"SELECT id_user, email, password FROM users where email = '{email}'"
    data = conn.execute(getdata).fetchall()
    return data


# ini query untuk login pake akun google
