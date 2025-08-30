import pytest
from django.urls import reverse
from accounts.api.v1.views import UserUpdateView
from rest_framework import status
from rest_framework.test import APIClient
from accounts.tests.fixtures import authenticated_manager, authenticated_worker, worker, manager

@pytest.mark.django_db
class TestAccountApi:
    
    # Test update account api
    # Manager can set the working time of workers each days
    def test_POST_update_account_status_201(self,worker , authenticated_manager):
        url = reverse("accounts:update", args=[worker.user.user_slug])
        data = {
            "start_time": "09:00",
            "end_time": "17:00",
        }
        response = authenticated_manager.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_POST_update_account_status_400(self,worker , authenticated_manager):
        url = reverse("accounts:update", args=[worker.user.user_slug])
        data = {
            "start_time": "invalid_time",
            "end_time": "17:00",
        }
        response = authenticated_manager.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_POST_update_account_status_401(self,worker):
        client = APIClient()
        url = reverse("accounts:update", args=[worker.user.user_slug])
        data = {
            "start_time": "09:00",
            "end_time": "17:00",
        }
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_POST_update_account_status_403(self,worker , authenticated_worker):
        url = reverse("accounts:update", args=[worker.user.user_slug])
        data = {
            "start_time": "09:00",
            "end_time": "17:00",
        }
        response = authenticated_worker.post(url, data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_POST_update_account_status_404(self, authenticated_manager):
        url = reverse("accounts:update", args=["invalid_username"])
        data = {
            "start_time": "09:00",
            "end_time": "17:00",
        }
        response = authenticated_manager.post(url, data, format='json')
        assert response.status_code == status.HTTP_404_NOT_FOUND


    # Test Profile Api
    # All logged in users can see their profile 
    # Manager can see the profile of all workers
    # Worker can see the profile of themselves
    def test_GET_profile_200(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("accounts:profile")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'manager' in response.data
        assert isinstance(response.data['manager'], dict)
        

    def test_GET_profile_200_manager(self, authenticated_manager):
        client = authenticated_manager
        url = reverse("accounts:profile")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'workers' in response.data
        assert isinstance(response.data['workers'], list)

    def test_GET_profile_401(self):
        client = APIClient()
        url = reverse("accounts:profile")
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Test logout API
    # All logged in users can logout
    def test_POST_logout_204(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("accounts:logout")
        data={
            "access_token": str(authenticated_worker.token.access_token),
            "refresh_token": str(authenticated_worker.token)
        }
        response = client.post(url,data,format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_POST_logout_401(self):
        client = APIClient()
        url = reverse("accounts:logout")
        response = client.post(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    # Test login API and token refresh API
    # They use default views from rest_framework_simplejwt
    # Only test for authentication and permission
    def test_POST_not_authenticated_can_login(self,worker):
        client = APIClient()
        url = reverse("accounts:login")
        data = {
            "username": worker.user.username,
            "password": "testpassword"
        }
        response = client.post(url,data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_POST_refresh_token_401(self):
        client = APIClient()
        url = reverse("accounts:refresh_token")
        data = {
            "refresh": "invalid_token"
        }
        response = client.post(url,data=data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

