from pytest import raises, fixture
from fastapi import Depends
from sqlalchemy.orm import Session
from src.login.user import User
from src.ddbb.crud.user import get_users, get_user_by_username, get_user_by_email, get_user_by_id, get_user, \
    create_user, update_user, delete_user
from src.ddbb.models.user import User as UserDDBBModel
from src.ddbb.models.user import Base
from tests.ddbb.database import SessionLocal, engine
from tests.utils import encrypt


Base.metadata.create_all(bind=engine)
test_users_data: list[dict] = [
    {
        'username': "test_user_one",
        'email': "user_1@test.es",
        'password': encrypt("test_1_password")
    },
    {
        'username': "test_user_two",
        'email': "user_2@test.es",
        'password': encrypt("test_2_password")
    },
    {
        'username': "test_user_three",
        'email': "user_3@test.es",
        'password': encrypt("test_3_password")
    }
]


class TestUserDDBBModel:
    db: Session = None 

    @classmethod
    def setup_class(cls):
        """
        Prepare the database before test
        """
        cls.db = SessionLocal()
        cls.db.query(UserDDBBModel).delete()
        cls.db.add(UserDDBBModel(**test_users_data[0]))
        cls.db.add(UserDDBBModel(**test_users_data[1]))
        cls.db.add(UserDDBBModel(**test_users_data[2]))
        cls.db.commit()
        cls.db.close()

    @classmethod
    def teardown_class(cls):
        """
        Prepare the database after test
        """
        cls.db = SessionLocal()
        cls.db.query(UserDDBBModel).delete()
        cls.db.commit()
        cls.db.close()

    def setup_method(self, method):
        self.db = SessionLocal()

    def teardown_method(self, method):
        self.db.close()

    def test_get_users(self):
        """
        Test get users from database.
        """
        users: list[User] = get_users(self.db)
        assert len(users) == len(test_users_data), \
            f'Error comparing users length: expected {len(test_users_data)}, got {len(users)}'

    def test_get_user_by_id(self):
        """
        Test get user by id from database.
        """
        users: list[User] = get_users(self.db)
        test_user: User = User(**users[0].__dict__)
        db_user: User = User(**get_user_by_id(self.db, test_user.get_id()).__dict__)
        assert equals_user(test_user, db_user), \
            f'Error comparing Users: expected {users[0]}, got {db_user}.'

    def test_get_user_by_username(self):
        """
        Test get user by username from database.
        """
        users: list[User] = get_users(self.db)
        test_user: User = User(**users[0].__dict__)
        db_user: User = User(**get_user_by_username(self.db, test_user.get_username()).__dict__)
        assert equals_user(test_user, db_user), \
            f'Error comparing Users: expected {users[0]}, got {db_user}.'

    def test_get_user_by_email(self):
        """
        Test get user by email from database.
        """
        users: list[User] = get_users(self.db)
        test_user: User = User(**users[0].__dict__)
        db_user: User = User(**get_user_by_email(self.db, test_user.get_email()).__dict__)
        assert equals_user(test_user, db_user), \
            f'Error comparing Users: expected {users[0]}, got {db_user}.'

    def test_get_user(self):
        """
        Test get user from database.
        """
        users: list[User] = get_users(self.db)
        test_user: User = User(**users[0].__dict__)
        db_user: User = User(**get_user(self.db, test_user).__dict__)
        assert equals_user(test_user, db_user), \
            f'Error comparing Users: expected {users[0]}, got {db_user}.'

    def test_create_new_user(self) -> None:
        """
        Test create new user into the database
        """
        self.db.query(UserDDBBModel).delete()
        test_user: User = User(**test_users_data[0])
        create_user(self.db, test_user)
        db_user: User = User(**get_user(self.db, test_user).__dict__)
        assert equals_user(test_user, db_user, check_id=False), \
            f'Error comparing Users: expected {test_user}, got {db_user}.'
    
    def test_update_user(self) -> None:
        """
        Test update existing user into the database
        """
        self.db.query(UserDDBBModel).delete()
        create_user(self.db, User(**test_users_data[0]))
        created_user: User = User(**get_user(self.db, User(**test_users_data[0])).__dict__)
        updated_user = User(
            id=created_user.get_id(),
            username=created_user.get_username(),
            email=created_user.get_email(),
            password=created_user.get_password()
        )
        update_user(self.db, updated_user)
        db_user: User = User(**get_user(self.db, updated_user).__dict__)
        assert equals_user(updated_user, db_user, check_id=False), \
            f'Error comparing Users: expected {updated_user}, got {db_user}.'

    def test_delete_user(self) -> None:
        """
        Test delete existing user into the database
        """
        self.db.query(UserDDBBModel).delete()
        create_user(self.db, User(**test_users_data[0]))
        created_user: User = User(**get_user(self.db, User(**test_users_data[0])).__dict__)
        delete_user(self.db, created_user)
        db_user = get_user(self.db, User(**test_users_data[0]))
        assert db_user == None, \
            f'Error comparing Users: expected None, got {db_user}.'


def equals_user(test_user: User, new_user: User, check_id: bool = True) -> bool:
    if test_user.get_username() == new_user.get_username() \
        and test_user.get_email() == new_user.get_email() \
        and test_user.get_password() == new_user.get_password():
        return True if not check_id else test_user.get_id() == new_user.get_id()
    return False
