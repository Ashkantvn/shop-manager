import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
class TestAccountViews:
    def setup_method(self):
        self.client = Client()

    def test_login_view_GET_200(self):
        url = reverse('accounts:login')
        response = self.client.get(url)
        assert response.status_code == 200
        assert 'accounts/login.html' in [template.name for template in response.templates]

    def test_login_view_POST_302(self):
        url = reverse('accounts:login')
        response = self.client.post(
            url,
            data={
                'username': 'testuser',
                'password': 'password'
            }
        )
        assert response.status_code == 302
        # Check user is logged in
        is_authenticated = response.wsgi_request.user.is_authenticated
        assert is_authenticated, "User should be authenticated after login"


    def test_logout_view_POST_302(self, authenticated_client):
        url = reverse('accounts:logout')
        response = authenticated_client.post(url)
        assert response.status_code == 302
        # Check user is logged out
        is_authenticated = response.wsgi_request.user.is_authenticated
        assert not is_authenticated, "User should be logged out after logout"
    
    def test_logout_view_POST_not_authenticated_302(self):
        url = reverse('accounts:logout')
        response = self.client.post(url)
        assert response.status_code == 302