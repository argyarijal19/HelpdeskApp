from fastapi import APIRouter, Body
from repository.auth.auth_handler import signJWT
from repository.auth.login_repo import get_email
from cryptography.fernet import Fernet
from schemas.login import UserLoginSchema


login = APIRouter()


@login.post('/login', tags=["Login"])
async def login_tradisional(user: UserLoginSchema = Body(...)):
    emailFromdb = get_email(user.email)
    if emailFromdb:
        return signJWT(user.email)
    else:
        message = {
            'message': 'Email Yang Anda Gunakan Tidak Terdaftar',
            'status': 0
        }
    return message
