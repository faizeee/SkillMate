import pytest
import uuid

from backend.tests.utils.helpers import fake_image, fake_txt


def test_get_skills(client):
    response = client.get("/api/skills/")
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "data , file",
    [
        ({"name": "AWS", "skill_level_id": "2"}, None),
        ({"name": "AWS", "skill_level_id": "2"}, fake_image()),
    ],
)
@pytest.mark.asyncio
async def test_create_skill(
    async_client, reset_db_state_for_session, auth_header, data, file
):
    print(data)
    data["name"] = f"{data['name']}-{uuid.uuid4().hex[:6]}"
    files = {"file": file} if file else {}
    response = await async_client.post(
        "/api/skills/", data=data, files=files, headers=auth_header
    )
    print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]


@pytest.mark.asyncio
async def test_create_duplicate_skill(async_client, auth_header):
    payload = {"name": "Python", "skill_level_id": "1"}
    # client.post("/api/skills/",json=payload,)
    response = await async_client.post(
        "/api/skills/", data=payload, headers=auth_header
    )
    # print("RESPONSE TEXT:",response.text)
    assert response.status_code == 409


@pytest.mark.parametrize(
    "data , file , status_code",
    [
        pytest.param({}, None, 422, id="missing-all-fields"),
        pytest.param(
            {},
            fake_image(),
            422,
            id="missing-all-except-image",
        ),
        pytest.param({"skill_level_id": "1"}, None, 422, id="missing-skill-name"),
        pytest.param({"name": "c++"}, None, 422, id="missing-skill-level-id"),
        pytest.param(
            {"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"},
            fake_txt(),
            400,
            id="invalid-file-type",
        ),
        pytest.param(
            {"name": f"AWS-{uuid.uuid4().hex}", "skill_level_id": "2"},
            fake_image(6),
            400,
            id="invalid-file-size",
        ),  # Invalid file size i.e 6mb file size
    ],
)
@pytest.mark.asyncio
async def test_invalid_payload(async_client, auth_header, data, file, status_code):
    files = {"file": file} if file else {}
    response = await async_client.post(
        "/api/skills/", data=data, files=files, headers=auth_header
    )
    print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == status_code


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
