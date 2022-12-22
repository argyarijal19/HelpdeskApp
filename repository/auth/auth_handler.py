import time
import jwt
from typing import Dict
import os

JWT_SECRET = os.getenv("secret")
JWT_ALGORTHM = os.getenv("algorithm")


def token_response(token: str):
    return {
        'access_token': token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORTHM)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decode_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORTHM])
        return decode_token if decode_token["expires"] >= time.time() else None
    except:
        return {}
