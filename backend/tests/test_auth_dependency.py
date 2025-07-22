from main import app
from fastapi import Depends
from models.user import User
from services.auth_service import get_current_user
from core.auth import create_access_token

def test_get_current_user_valid_token(client,current_user):
    token = current_user['access_token']
    
    #defining temporary route
    temp_route_url = '/test-user'
    @app.get(temp_route_url)
    def protected_route(test_user: User = Depends(get_current_user)):
        return {"username": test_user.username}
    #sending request to temporary route
    response = client.get(temp_route_url,headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()['username'] == current_user['user']['username']

def test_invalid_token_signature(client):
    fake_token = "this.is.not.valid"
    
    #defining temporary route
    temp_route_url = '/test-invalid'
    @app.get(temp_route_url)
    def protected_route(test_user: User = Depends(get_current_user)):
        return {"username": test_user.username}
    
    #sending request to temporary route
    response = client.get(temp_route_url,headers={"Authorization": f"Bearer {fake_token}"})
    assert response.status_code == 401
    assert response.json()['detail'] == "Invalid Token"

def test_token_missing_sub_claim(client):
    token = create_access_token({"some":"data"})

    #defining temporary route
    temp_route_url = '/test-missing-sub'
    @app.get(temp_route_url)
    def protected_route(test_user : User = Depends(get_current_user)):
        return {"username":test_user.username}
    
    #sending request to temporary route
    response = client.get(temp_route_url,headers={"Authorization":f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()['detail'] == "Invalid User Token"

def test_user_not_in_db(client):
    token = create_access_token({"sub":"ghostuser"})

    #defining temporary route
    temp_route_url = "/test-no-user"
    @app.get(temp_route_url)
    def protected_route(test_user:User = Depends(get_current_user)):
        return {"username":test_user.username}
    #sending request to temporary route
    response = client.get(temp_route_url,headers={"Authorization":f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()['detail'] == "User not found"

def test_missing_authorization_header(client):
    #defining temporary route
    temp_route_url = "/test-missing-header"
    @app.get(temp_route_url)
    def protected_route(test_user:User = Depends(get_current_user)):
        return {"username":test_user.username}
    #sending request to temporary route
    response = client.get(temp_route_url)
    assert response.status_code == 401
    assert "Not authenticated" in response.json()['detail']

def test_expired_token(client):
    token = create_access_token({"sub":"testuser1"},expires_delta=-10) # Already expired

    temp_route_url  = "/test-expired"
    @app.get(temp_route_url)
    def protected_route(test_user:User = Depends(get_current_user)):
        return {"username":test_user.username}
    response = client.get(temp_route_url,headers={"Authorization":f"Bearer {token}"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid Token"