from fastapi.testclient import TestClient
from fastapi import status


def test_admin_access(client: TestClient, auth_header_for_admin):
    response = client.get("/api/admin/dashboard", headers=auth_header_for_admin)
    assert response.status_code == status.HTTP_200_OK


def test_user_forbidden_admin(client: TestClient, auth_header):
    response = client.get("/api/admin/dashboard", headers=auth_header)
    assert response.status_code == status.HTTP_403_FORBIDDEN
