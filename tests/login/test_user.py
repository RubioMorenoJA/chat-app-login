from pytest import raises
from src.login.user import User
from tests.utils import encrypt


class TestUser:
    def test_create_user_ok(self) -> None:
        """
        Test creating new user successfully
        """
        id: int = 0
        username: str = 'pope_test'
        email: str = 'pope@chatapp.com'
        password: str = '1Qaz2Wsx'

        user = User(
            id=id,
            username=username,
            email=email,
            password=password
        )
        assert id == user.get_id(), \
            f'Error comparing id: expected {id}, got {user.get_id}'
        assert username == user.get_username(), \
            f'Error comparing username: expected {username}, got {user.get_username}'
        assert email == user.get_email(), \
            f'Error comparing email: expected {email}, got {user.get_email}'
        assert encrypt(password) == user.get_password(), \
            f'Error comparing password: expected {password}, got {user.password}'

    def test_set_user_ok(self) -> None:
        """
        Test create object from existing user successfully
        """
        id: int = 0
        username: str = 'pope_test'
        email: str = 'pope@chatapp.com'
        password: str = encrypt('1Qaz2Wsx')

        user = User(
            id=id,
            username=username,
            email=email,
            password=password
        )
        assert id == user.get_id(), \
            f'Error comparing id: expected {id}, got {user.get_id}'
        assert username == user.get_username(), \
            f'Error comparing username: expected {username}, got {user.get_username}'
        assert email == user.get_email(), \
            f'Error comparing email: expected {email}, got {user.get_email}'
        assert password == user.get_password(), \
            f'Error comparing password: expected {password}, got {user.password}'

    def test_username_empty(self) -> None:
        """
        Test empty username
        """
        username = ''
        with raises(ValueError) as excinfo:
            user = User(username=username)
        assert 'username cannot be empty' in str(excinfo.value)

    def test_username_with_spaces(self) -> None:
        """
        Test username with spaces
        """
        username = 'user name'
        with raises(ValueError) as excinfo:
            user = User(username=username)
        assert 'username cannot have spaces' in str(excinfo.value)
        
    def test_username_with_number(self) -> None:
        """
        Test username with numbers
        """
        username = 'user1name2'
        with raises(ValueError) as excinfo:
            user = User(username=username)
        assert 'username cannot contains numbers' in str(excinfo.value)

    def test_email_empty(self) -> None:
        """
        Test empty email
        """
        email = ''
        with raises(ValueError) as excinfo:
            user = User(email=email)
        assert 'email cannot be empty' in str(excinfo.value)
    
    def test_email_missing_symbols_1(self) -> None:
        """
        Test email missing @
        """
        email = 'popechatapp.com'
        with raises(ValueError) as excinfo:
            user = User(email=email)
        assert 'email wrong spelling' in str(excinfo.value)

    def test_email_missing_symbols_2(self) -> None:
        """
        Test email missing . extension
        """
        email = 'pope@chatappcom'
        with raises(ValueError) as excinfo:            
            user = User(email=email)                 
        assert 'email wrong spelling' in str(excinfo.value)

    def test_password_empty(self) -> None:
        """
        Test empty password
        """
        password = ''        
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert 'password cannot be empty' in str(excinfo.value)
    
    def test_password_wrong_len_1(self) -> None:
        """
        Test password length lower than expected
        """
        password = '1Qaz2'        
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert f'password has not the correct length: {password.__len__()}' in str(excinfo.value)

    def test_password_wrong_len_2(self) -> None:
        """
        Test password length higher than expected
        """
        password = '1Qaz2Wsx3Ed'        
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert f'password has not the correct length: {password.__len__()}' in str(excinfo.value)

    def test_password_wrong_spelling_1(self) -> None:
        """
        Test password wrong spelling without lower case letters
        """
        password = '1QAZ2WSX'        
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert 'password does not match the correct form' in str(excinfo.value)
    
    def test_password_wrong_spelling_2(self) -> None:
        """
        Test password wrong spelling without upper case letters
        """
        password = '1qaz2wsx'        
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert 'password does not match the correct form' in str(excinfo.value)

    def test_password_wrong_spelling_3(self) -> None:
        """
        Test password wrong spelling without numbers
        """
        password = 'QazWsxEdc'        
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert 'password does not match the correct form' in str(excinfo.value)
    
    def test_password_wrong_hashed(self) -> None:
        """
        Test password wrong spelling without lower case letters
        """
        password = encrypt('1Qaz2Wsx3E')[:62]
        with raises(ValueError) as excinfo:
            user = User(password=password)
        assert f'password has not the correct length: {password.__len__()}' in str(excinfo.value)
