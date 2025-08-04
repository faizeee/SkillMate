from main import app
from services.permissions import admin_only, user_only
from services.auth_service import get_current_user
from models import User
from fastapi import Depends, status
from fastapi.testclient import TestClient


def test_only_admin_route_with_correct_user(client: TestClient, admin_user):
    token = admin_user["access_token"]

    temp_route_url = "/admin/dashboard"

    @app.get(temp_route_url, dependencies=[Depends(admin_only)])
    def protected_route(user: User = Depends(get_current_user)):
        return {"username": user.username}

    response = client.get(temp_route_url, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == admin_user["user"]["username"]


def test_only_admin_route_with_wrong_user(client: TestClient, current_user):
    token = current_user["access_token"]

    temp_route_url = "/admin/dashboard"

    @app.get(temp_route_url, dependencies=[Depends(admin_only)])
    def protected_route(user: User = Depends(get_current_user)):
        return {"username": user.username}

    response = client.get(temp_route_url, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_only_user_route_with_admin_user(client: TestClient, admin_user):
    token = admin_user["access_token"]

    temp_route_url = "/test-admin-on-user"

    @app.get(temp_route_url, dependencies=[Depends(user_only)])
    def protected_route(user: User = Depends(get_current_user)):
        return {"username": user.username}

    response = client.get(temp_route_url, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == admin_user["user"]["username"]


def test_only_route_route_with_simple_user(client: TestClient, current_user):
    token = current_user["access_token"]

    temp_route_url = "/test-admin-on-user"

    @app.get(temp_route_url, dependencies=[Depends(user_only)])
    def protected_route(user: User = Depends(get_current_user)):
        return {"username": user.username}

    response = client.get(temp_route_url, headers={"Authorization": f"Bearer {token}"})
    print(f"RESPONSE TEXT -> {response.status_code} : {response.text}")
    assert response.status_code == status.HTTP_200_OK
