import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv

load_dotenv()

def create_token(id: int, role: str) -> str:
    today = datetime.now(timezone.utc)
    return jwt.encode(payload={
        'iss': 'khunly.be',
        'iat': today.timestamp(),
        'exp': timedelta(minutes=15) + today,
        'role': role,
        'sub': str(id)
    }, key=os.getenv('JWT_SECRET'), algorithm='HS256')

def verify_token(token: str) -> dict:
    try:
        return jwt.decode(token, key=os.getenv('JWT_SECRET'), algorithms=['HS256'])
    except jwt.exceptions.DecodeError as e:
        raise ValueError(e) from e