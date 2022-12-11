from fastapi import APIRouter
from src.login.user import User


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('')
async def get_token():
    pass

@router.get('')
async def get_user():
    pass

@router.post('')
async def create_new_user():
    pass

@router.put('')
async def modify_user():
    pass

@router.delete('')
async def delete_user():
    pass
