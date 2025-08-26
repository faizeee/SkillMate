import pytest
import uuid

from backend.tests.utils.helpers import fake_image, fake_txt, mock_save_file


def test_get_skills(client):
    response = client.get("/api/skills/")
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "data , file",
    [
        ({"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"}, None),
        ({"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"}, fake_image()),
    ],
    ids=["create-skill-without-file", "create-skill-with-file"],
)
@pytest.mark.asyncio
async def test_create_skill(
    async_client, reset_db_state_for_session, auth_header, data, file, mocker, tmp_path
):
    files = {}
    expected_icon_path = None
    if file:
        files = {"file": file}
        patch_target = "controllers.skill_controller.save_file"
        expected_icon_path = mock_save_file(mocker, patch_target, tmp_path, file)

    response = await async_client.post(
        "/api/skills/", data=data, files=files, headers=auth_header
    )
    print("RESPONSE TEXT:", response.text)  # print raw error message
    print("RESPONSE:", response.json())  # print raw error message
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["name"] == data["name"]
    if file:
        assert res_json["icon_path"] == expected_icon_path


@pytest.mark.asyncio
async def test_create_duplicate_skill(async_client, auth_header):
    payload = {"name": "Python", "skill_level_id": "1"}
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


@pytest.mark.parametrize(
    "data, file",
    [
        pytest.param(
            {"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"},
            None,
            id="update-without-file-with-valid-user-and-data",
        ),
        pytest.param(
            {"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"},
            fake_image(),
            id="update-with-file-valid-user-and-data",
        ),
    ],
)
@pytest.mark.asyncio
async def test_update_skill_with_valid_user_and_data(
    async_client, auth_header_for_admin, data, file, mocker, tmp_path
):
    skill_id = 1
    files = {}
    expected_icon_path = None
    if file:
        files = {"file": file}
        patch_target = "controllers.skill_controller.save_file"
        expected_icon_path = mock_save_file(mocker, patch_target, tmp_path, file)
    response = await async_client.put(
        f"/api/skills/{skill_id}", data=data, files=files, headers=auth_header_for_admin
    )
    print("RESPONSE TEXT:", response.text)  # print raw error message
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["name"] == data["name"]
    assert response_data["id"] == skill_id
    if file:
        assert response_data["icon_path"] is not None
        assert response_data["icon_path"] == expected_icon_path


@pytest.mark.asyncio
async def test_update_skill_with_invalid_user(async_client, auth_header):
    unique_name = f"AWS-{uuid.uuid4().hex[:6]}"
    skill_id = 1
    payload = {"name": unique_name, "skill_level_id": "2"}
    response = await async_client.put(
        f"/api/skills/{skill_id}", data=payload, headers=auth_header
    )
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 403


@pytest.mark.parametrize(
    "skill_id, data, file, expected_status_code",
    [
        pytest.param(2, {}, None, 422, id="update-with-all-missing"),
        pytest.param(
            2, {}, fake_image(), 422, id="update-with-all-missing-except-image"
        ),
        pytest.param(
            2, {"skill_level_id": "1"}, fake_image(), 422, id="update-with-missing-name"
        ),
        pytest.param(
            2,
            {"name": "c++"},
            fake_image(),
            422,
            id="update-with-missing-skill_level_id",
        ),
        pytest.param(
            99999,
            {"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"},
            None,
            404,
            id="update-with-valid-data-but-invalid-skill-id",
        ),
        pytest.param(
            2,
            {"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"},
            fake_image(6),
            400,
            id="update-with-valid-user-and-data-but-invalid-file-size",
        ),
        pytest.param(
            2,
            {"name": f"AWS-{uuid.uuid4().hex[:6]}", "skill_level_id": "2"},
            fake_txt(),
            400,
            id="update-with-valid-user-and-data-but-invalid-file-type",
        ),
    ],
)
@pytest.mark.asyncio
async def test_update_skill_with_invalid_payload(
    async_client, auth_header_for_admin, skill_id, data, file, expected_status_code
):
    files = {"file": file} if file else {}
    response = await async_client.put(
        f"/api/skills/{skill_id}", data=data, files=files, headers=auth_header_for_admin
    )
    print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == expected_status_code


@pytest.mark.asyncio
async def test_update_skill_with_duplicate_skill_name(
    async_client, auth_header_for_admin, reset_db_state
):
    data = {"name": "PHP", "skill_level_id": "1"}
    skill_id = 2
    response = await async_client.put(
        f"/api/skills/{skill_id}", data=data, headers=auth_header_for_admin
    )
    # print("RESPONSE TEXT:", response.text)  # print raw error message
    assert response.status_code == 409
