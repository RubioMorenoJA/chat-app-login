from fastapi import Header, HTTPException
from src.ddbb.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_application_json(content_type: str = Header()):
    if content_type != 'application/json':
        raise HTTPException(status_code=400, detail=f'Unsupported {content_type}. It must be application/json')
