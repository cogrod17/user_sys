from time import time
import jwt
from typing import Dict
from decouple import config
import time


JWT_ALGORITHM = config('JWT_ALGORITHM')
JWT_SECRET = config('JWT_SECRET')


def signJWT(userId: int) -> Dict[str, str]:
    payload = {
        "userId": userId,
        "expiry": time.time() + 60*60
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decode(token):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])


def verify_token(token: str):
    try:
        decoded = decode(token)
        return True if decoded['expiry'] >= time.time() else False
    except:
        return False


def is_self(token: str, id: int):
    try:
        decoded = decode(token)
        return True if decoded['userId'] == id else False
    except:
        return False
