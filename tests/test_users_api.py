import pytest
import requests

BASE_URL = "https://hr-challenge.dev.tapyou.com/api/test"


# USERS LIST TESTS
@pytest.mark.parametrize("gender, expected_status", [
    ("male", 200),
    ("female", 200),
    ("any", 200),
    ("", 400),
    ("invalid", 500)
])

def test_gender_query_edge_cases(gender, expected_status):
    url = f"{BASE_URL}/users"
    if gender:
        url += f"?gender={gender}"
    response = requests.get(url)
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

def test_user_15_always_in_response():
    user_id = 15
    for gender in ["male", "female", "any"]:
        response = requests.get(f"{BASE_URL}/users?gender={gender}")
        assert response.status_code == 200
        ids = response.json().get("result", [])
        assert user_id in ids, f"User {user_id} not found in {gender} filter"

def test_wrong_users_in_filters():
    male_resp = requests.get(f"{BASE_URL}/users?gender=male").json()
    female_resp = requests.get(f"{BASE_URL}/users?gender=female").json()
    assert 911 not in male_resp["result"], "User 911 incorrectly appears in male list"
    assert 300 not in female_resp["result"], "User 300 incorrectly appears in female list"

def test_any_filter_ids_and_missing_user():
    response = requests.get(f"{BASE_URL}/users?gender=any").json()
    ids = response["result"]
    assert 0 in ids, "ID 0 missing"
    assert 212 in ids, "ID 212 missing"

    user_response = requests.get(f"{BASE_URL}/user/212")
    user_json = user_response.json()
    assert user_json["result"] is None, "Expected user 212 to be missing"

# USER ID TESTS
@pytest.mark.parametrize("user_id, expected_status", [
    ("abc", 400),
    ("", 500),
    (999999, 200),
    (0, 500),
])
def test_user_by_invalid_id(user_id, expected_status):
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == expected_status

def test_user_by_nonexistent_id_returns_null():
    response = requests.get(f"{BASE_URL}/user/999999")
    assert response.status_code == 200
    assert response.json()["result"] is None

def test_user_911_always_returns():
    response = requests.get(f"{BASE_URL}/user/911")
    assert response.status_code == 200
    user = response.json()["result"]
    assert user is not None
    assert int(user["id"]) == 911

# DATA FORMAT & PERFORMANCE TESTS
def test_registration_date_format():
    for gender in ["male", "female"]:
        ids = requests.get(f"{BASE_URL}/users?gender={gender}").json()["result"]
        if not ids:
            continue
        user = requests.get(f"{BASE_URL}/user/{ids[0]}").json()["result"]
        date_str = user.get("registrationDate", "")
        assert "T" in date_str, f"{gender} user date not in ISO format: {date_str}"

@pytest.mark.parametrize("user_id", [2, 4, 6, 8])
def test_even_id_delay(user_id):
    import time
    start = time.time()
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    duration = time.time() - start
    assert response.status_code == 200
    assert duration < 3, f"Request for even id {user_id} too slow: {duration:.2f}s"