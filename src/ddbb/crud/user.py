from sqlalchemy.orm import Session
from src.ddbb.utils import add_to_ddbb, delete_from_ddbb
from src.ddbb.models.user import User as UserDDBBModel
from src.login.user import User


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserDDBBModel).filter(UserDDBBModel.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(UserDDBBModel).filter(UserDDBBModel.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserDDBBModel).filter(UserDDBBModel.email == email).first()

def get_user(db: Session, user: User):
    return db.query(UserDDBBModel).filter(
        UserDDBBModel.username == user.get_username(),
        UserDDBBModel.email == user.get_email(),
        UserDDBBModel.password == user.get_password()
    ).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserDDBBModel).offset(skip).limit(limit).all()

def create_user(db: Session, new_user: User):
    db_user = UserDDBBModel(**new_user.dict())  # username=new_user.get_username(), email=new_user.get_email(), password=new_user.get_password())
    add_to_ddbb(db, db_user)
    return db_user

def update_user(db: Session, update_user: User):
    return db.query(UserDDBBModel).filter(UserDDBBModel.id == update_user.get_id()).update(update_user.dict())

def delete_user(db: Session, delete_user: User):
    db_user = get_user(db, delete_user)
    delete_from_ddbb(db, db_user)
    return db_user
