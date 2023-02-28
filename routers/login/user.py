import traceback
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import ObjectDeletedError
from dependencies import get_db, verify_application_json
from src.login.user import User
from src.ddbb.database import create_db_tables, Base, engine
from src.ddbb.crud.user import *


router = APIRouter(
    prefix='/users',
    tags=['users'],
    dependencies=[Depends(verify_application_json)],
    responses={
        200: {"description": "Ok"},
        201: {"description": "User created"},
        400: {"description": "User Bad Request"},
        404: {"description": "User Not Found"},
        500: {"description": "User Server Error"},
        501: {"description": "User method not implemented yet"},
    }
)
create_db_tables(Base, engine)


@router.get('/token')
async def get_token():
    raise HTTPException(status_code=501)

@router.get('/{id}', response_model=User, response_model_exclude={'password'})
async def get_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, id)
    if db_user is None:
        raise HTTPException(status_code=404)
    return db_user

@router.post('/create', response_model=User, response_model_exclude={'password'})
async def create_new_user(new_user: User, db: Session = Depends(get_db)):
    try:
        create_user(db, new_user)
    except SQLAlchemyError as exc:
        raise SystemError(f'Unable to save user:\n{exc.args}\n{traceback.format_exc}')
    return new_user

@router.put('/update', response_model=User, response_model_exclude={'password'})
async def modify_user(update_user: User, db: Session = Depends(get_db)):
    db_user = update_user(db, update_user)
    if db_user is None:
        raise HTTPException(status_code=200)
    return db_user

@router.delete('/delete/{id}', response_model=User)
async def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    raise HTTPException(status_code=501)

@router.delete('/delete', response_model=User)
async def delete_user(delete_user: User, db: Session = Depends(get_db)):
    return delete_user(db, delete_user)
