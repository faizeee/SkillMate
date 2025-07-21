import pytest

def test_register_user(client):
    username = "testuser1"
    payload = {"username":username,"password":"12345678"}
    response = client.post("/api/register/",json=payload)
    assert response.status_code == 200
    assert response.json()['username'] == username

def test_register_duplicate_user(client):
    username = "testuser1"
    payload = {"username":username,"password":"12345678"}
    client.post("/api/register/",json=payload)
    response = client.post("/api/register/",json=payload)
    print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == 400
    assert response.json()['detail'] == "Username already Exits"


@pytest.mark.parametrize("payload",[
    {},
    {"username":"testuser1"},
    {"password":"1234567"}
])
def test_register_invalid_payload(client,payload):
    response = client.post("/api/register/",json=payload)
    assert response.status_code == 422

@pytest.mark.parametrize("payload",[
    {"username":"test","password":"12345678"},
    {"username":"testuser","password":"1234567"}
])
def test_register_invalid_min_length_payload(client,payload):
    response = client.post("/api/register/",json=payload)
    assert response.status_code == 422
    assert response.json()["detail"][0]['type'] == "string_too_short"


def test_login_user(client):
    username = "testuser1"
    payload = {"username":username,"password":"12345678"}
    
    client.post("/api/register/",json=payload)
    response = client.post("/api/login/",json=payload)
    assert response.status_code == 200
    assert response.json()['token_type'] == "bearer"

@pytest.mark.parametrize("payload",[
    {"username":"testuser1","password":"123456789"},
    {"username":"testuser2","password":"12345679"}
])
def test_login_invalid_password(client,payload):
    response = client.post("/api/login/",json=payload)
    print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid Username or Password"

@pytest.mark.parametrize("payload",[
    {},
    {"username":"testuser1"},
    {"password":"12345678"}
])
def test_login_invalid_payload(client,payload):
    response = client.post("/api/login/",json=payload)
    assert response.status_code == 422

    