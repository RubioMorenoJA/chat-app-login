from os import path
from fastapi.testclient import TestClient
from main import app
from tests.utils import load_resource, generate_path


client = TestClient(app)
test_users_data: list[dict] = load_resource(generate_path(path.abspath(""), "tests", "resources", "test_users.json"))


class TestLoginUserAPI:

    def test_get_user_by_id():    
        # response = client.get()
        pass