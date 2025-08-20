import pytest
import uuid


def test_get_skills(client):
    response = client.get("/api/skills/")
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert isinstance(response.json(), list)


pytest.mark.asyncio


async def test_create_skill(async_client, reset_db_state, auth_header):
    unique_name = f"AWS-{uuid.uuid4().hex[:6]}"
    payload = {"name": unique_name, "skill_level_id": "2"}
    response = await async_client.post(
        "/api/skills/", json=payload, headers=auth_header
    )
    print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert response.json()["name"] == unique_name


def test_create_duplicate_skill(client, auth_header):
    payload = {"name": "Python", "skill_level_id": "1"}
    # client.post("/api/skills/",json=payload,)
    response = client.post("/api/skills/", json=payload, headers=auth_header)
    # print("RESPONSE TEXT:",response.text)
    assert response.status_code == 409


@pytest.mark.parametrize(
    "payload",
    [
        {},  # missing all fields
        {"skill_level_id": "1"},  # missing name
        {"name": "c++"},  # missing skill_level_id
    ],
)
def test_invalid_payload(client, auth_header, payload):
    response = client.post("/api/skills", json=payload, headers=auth_header)
    # print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == 422


def test_get_skill_by_valid_id(client, reset_db_state, auth_header):
    response = client.get("/api/skills/1", headers=auth_header)
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_skill_by_invalid_id(client, auth_header):
    response = client.get("/api/skills/9999", headers=auth_header)
    assert response.status_code == 404


def test_delete_skill_by_valid_id(client, reset_db_state, auth_header):
    response = client.delete("/api/skills/1", headers=auth_header)
    assert response.status_code == 200
    assert response.json()["success"] is True


def test_skill_by_invalid_id(client, auth_header):
    response = client.delete("/api/skills/9999", headers=auth_header)
    assert response.status_code == 404


def test_get_skill_levels(client):
    response = client.get("/api/skills/levels")
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_skill_levels_error(client, drop_all_tables_for_error_test):
    response = client.get("/api/skills/levels")
    print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == 500
    assert any(
        phrase in response.json()["detail"]
        for phrase in ["no such table", "does not exist", "UndefinedTable"]
    )


def test_get_skill_error(client, drop_all_tables_for_error_test):
    response = client.get("/api/skills")
    print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == 500
    assert any(
        phrase in response.json()["detail"]
        for phrase in ["no such table", "does not exist", "UndefinedTable"]
    )
    # assert "no such table" in response.json()["detail"]


def test_update_skill_with_valid_user_and_data(client, auth_header_for_admin):
    unique_name = f"AWS-{uuid.uuid4().hex[:6]}"
    skill_id = 1
    payload = {"name": unique_name, "skill_level_id": "2"}
    response = client.put(
        f"/api/skills/{skill_id}", json=payload, headers=auth_header_for_admin
    )
    print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert response.json()["name"] == unique_name
    assert response.json()["id"] == skill_id


def test_update_skill_with_invalid_user(client, auth_header):
    unique_name = f"AWS-{uuid.uuid4().hex[:6]}"
    skill_id = 1
    payload = {"name": unique_name, "skill_level_id": "2"}
    response = client.put(f"/api/skills/{skill_id}", json=payload, headers=auth_header)
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 403


@pytest.mark.parametrize(
    "payload, expected_status_code",
    [
        ({}, 422),  # missing all fields
        ({"skill_level_id": "1"}, 422),  # missing name
        ({"name": "c++"}, 422),  # missing skill_level_id
        # ({"name": "PHP", "skill_level_id": "1"}, 409),  # duplicate name
    ],
)
def test_update_skill_with_invalid_payload(
    client, auth_header_for_admin, payload, expected_status_code
):
    skill_id = 2
    response = client.put(
        f"/api/skills/{skill_id}", json=payload, headers=auth_header_for_admin
    )
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == expected_status_code


def test_update_skill_with_invalid_skill_name(
    client, auth_header_for_admin, reset_db_state
):
    payload = {"name": "PHP", "skill_level_id": "1"}
    expected_status_code = 409
    skill_id = 2
    response = client.put(
        f"/api/skills/{skill_id}", json=payload, headers=auth_header_for_admin
    )
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == expected_status_code
