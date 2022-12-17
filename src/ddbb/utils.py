from sqlalchemy.orm import Session


def add_to_ddbb(db: Session, object) -> None:
    """
    Add new object into the database.

    Args:
        db (Session): current db session
        object (_type_): object to save
    """
    db.add(object)
    db.commit()


def delete_from_ddbb(db: Session, object) -> None:
    """
    Delete object in the database.

    Args:
        db (Session): current db session
        object (_type_): object to delete
    """
    db.delete(object)
    db.commit()
