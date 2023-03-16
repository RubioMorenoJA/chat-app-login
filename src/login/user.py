"""
    _summary_
"""
import re
from pydantic import BaseModel, validator, ValidationError
from hashlib import sha256


class User(BaseModel):
    id: int = 0
    username: str = ''
    email: str = ''
    password: str = ''

    class Config:
        orm_mode = True

    @validator('id')
    def set_id(cls, id: int) -> int:
        if type(id) != int:
            return int(id)
        return id                        
        
    @validator('username')
    def set_username(cls, username: str) -> str:
        if username == '':
            raise ValueError('username cannot be empty')
        if re.findall(r'\s+', username):
            raise ValueError('username cannot have spaces')
        if re.findall(r'[0-9]+', username):
            raise ValueError('username cannot contains numbers')
        return username

    @validator('email')
    def set_email(cls, email: str) -> str:
        if email == '':
            raise ValueError('email cannot be empty')
        if not re.fullmatch(r'[a-zA-Z0-9._\-+]+@[a-zA-Z0-9._\-+]+\.[a-z]{1,4}', email):
            raise ValueError('email wrong spelling')
        return email
    
    @validator('password')
    def set_password(cls, password: str) -> str:
        if password.__len__() == 64:
            return password
        if password == '':
            raise ValueError('password cannot be empty')
        if not 6 < password.__len__() < 10:
            raise ValueError(f'password has not the correct length: {password.__len__()}')
        if not (re.findall(r'[a-z]+', password)
                and re.findall(r'[A-Z]+', password)
                and re.findall(r'[0-9]+', password)):
            raise ValueError('password does not match the correct form')
        return sha256(f'{password}'.encode('utf-8')).hexdigest()

    def get_id(self) -> int:
        return self.id

    def get_username(self) -> str:
        return self.username

    def get_email(self) -> str:
        return self.email
    
    def get_password(self) -> str:
        return self.password
