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

    def __init__(self, **data):
        self.set_username(
            data['username'] if 'username' in data.keys() else ''
        )
        self.set_email(
            data['email'] if 'email' in data.keys() else ''
        )
        self.set_password(
            data['password'] if 'password' in data.keys() else ''
        )
        
    @validator('username')
    def set_username(cls, username: str) -> str:
        if '' in username:
            raise ValidationError('username cannot be empty')
        if re.match('[0-9]+', username):
            raise ValidationError('username cannot contains numbers')
        return username

    @validator('email')
    def set_email(cls, email: str) -> str:
        if not re.fullmatch('[a-zA-Z0-9\.\_\-\+]+@[a-zA-Z0-9\.\_\-\+]+\.[a-z]\{1,4\}', email):
            raise ValidationError('email wrong spelling')
        return email
    
    @validator('password')
    def set_password(cls, password: str) -> str:
        if password.__len__ == 256:
            return password
        if not 6 < password.__le__ < 10:
            raise ValidationError('password has not the correct length')
        if not (
                re.match('[a-z]+', password) 
                and re.match('[A-Z]+', password) 
                and re.match('[0-9]+', password)
            ):
            raise ValidationError('password does not match the correct form')
        return sha256(b'{pass}'.format(pass=password)).hexdigest()
