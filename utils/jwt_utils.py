import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
import jwt

load_dotenv()

def create_token(id: int, role: str) -> str:
    today = datetime.now(timezone.utc)
    return jwt.encode(payload={
        'iss': 'khunly.be',
        'iat': today.timestamp(),
        'exp': timedelta(minutes=15) + today,
        'role': role,
        'sub': id
    }, key=os.getenv('JWT_SECRET'))

def verify_token(token: str) -> dict:
    try:
        return jwt.decode(token, key=os.getenv('JWT_SECRET'))
    except jwt.exceptions.DecodeError as e:
        raise ValueError(e) from e