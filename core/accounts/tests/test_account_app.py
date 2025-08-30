import pytest
from accounts.tests.fixtures import authenticated_manager, custom_user
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestAccountApp:
    # Test for app profile view
    def test_app_GET_profile_view(self, authenticated_manager):
        """
        Tests that the app profile view returns a 200 response with the correct template.
        """
        client = authenticated_manager
        url = reverse("app-accounts:app-profile")
        response = client.get(url)
        assert response.status_code == 200
        assert 'accounts/profile.html' in [t.name for t in response.templates]

    # Test for app login view
    def test_app_GET_login_view(self):
        """
        Tests that the app login view returns a 200 response with the correct template.
        """
        client = Client()
        url = reverse("app-accounts:login")
        response = client.get(url)
        assert response.status_code == 200
        assert 'accounts/login.html' in [t.name for t in response.templates]

    def test_app_POST_login_view(self, custom_user):
        """
        Tests that the app login view redirects to the profile page after successful login.
        """
        client = Client()
        url = reverse("app-accounts:login")
        
        # Simulate a login
        response = client.post(url, {'username': custom_user.username, 'password': 'testpassword'})
        
        # Check if the user is redirected to the profile page
        assert response.status_code == 302
        assert response.url == reverse("app-accounts:profile")

