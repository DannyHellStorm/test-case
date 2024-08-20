import os
import pytest
from dotenv import load_dotenv
from user_class import QaTestController

load_dotenv()

@pytest.fixture
def api_client():
    return QaTestController(baseUrl = os.getenv('URL'))

def test_get_users_by_gender(api_client):
    params = {
        'gender': 'female'
    }
    response = api_client.getUsersByGender('users', params)
    assert response == 200

def test_get_user_by_id(api_client):
    response = api_client.getUserById('user/5')
    assert response == 200


