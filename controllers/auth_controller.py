from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from dto.login_dto import LoginDTO
from dto.register_dto import RegisterDTO
from models.account import Account
from models.db import get_db
from utils import jwt_utils, password_utils

router = APIRouter(prefix='/auth')

@router.post('/register', status_code=201)
async def register(
    dto: Annotated[RegisterDTO, Body()], 
    session: Annotated[Session, Depends(get_db)]
):
    try: 
        account = Account(
            username=dto.username,
            email=dto.email,
            password_hash=password_utils.hash(dto.password),
            role=dto.role
        )
        session.add(account)
        session.flush()
    except:
        print('-----------------------------------')
        raise HTTPException(status_code=400, detail='Impossible de sauver cet account (vérifier vos données)')

@router.post('/login')
def login(
    dto: Annotated[LoginDTO, Body()], 
    session: Annotated[Session, Depends(get_db)]
):
    account = session.execute(
        select(Account).where(Account.username == dto.username)
    ).scalar()

    if not account or not password_utils.verify_password(
        dto.password, account.password_hash
    ):
        raise HTTPException(401)

    return {
        'access_token': jwt_utils.create_token(account.id, account.role)
    }
    