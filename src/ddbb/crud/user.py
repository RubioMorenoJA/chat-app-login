from sqlalchemy.orm import Session
from src.ddbb.utils import add_to_ddbb, delete_from_ddbb
from src.ddbb.models.user import User as UserDDBBModel
from src.login.user import User


__all__ = ['get_users', 'get_user_by_username', 'get_user_by_email', 'get_user_by_id', 'get_user',
           'create_user', 'update_user', 'delete_user', 'delete_user_by_id']

    
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
    # username=new_user.get_username(), email=new_user.get_email(), password=new_user.get_password())
    db_user = UserDDBBModel(**new_user.dict())
    add_to_ddbb(db, db_user)
    return db_user


def update_user(db: Session, updated_user: User):
    return db.query(UserDDBBModel).filter(UserDDBBModel.id == updated_user.get_id()).update(updated_user.dict())


def delete_user(db: Session, deleted_user: User):
    db_user = get_user(db, deleted_user)
    delete_from_ddbb(db, db_user)
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    """
    Deletes selected user by id
    Args:
        db:
        user_id:

    Returns:

    """
    db_user = get_user_by_id(db, user_id)
    delete_from_ddbb(db, db_user)
    return db_user
