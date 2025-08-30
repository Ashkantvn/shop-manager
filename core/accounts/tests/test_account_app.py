import pytest
from accounts.tests.fixtures import authenticated_manager
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestAccountApp:
    # Test for app profile view
    def test_app_profile_view(self, authenticated_manager):
        """
        Tests that the app profile view returns a 200 response with the correct template.
        """
        client = authenticated_manager
        url = reverse("app-accounts:app-profile")
        response = client.get(url)
        assert response.status_code == 200
        assert 'accounts/profile.html' in [t.name for t in response.templates]

    # Test for app login view
    def test_app_login_view(self):
        """
        Tests that the app login view returns a 200 response with the correct template.
        """
        client = Client()
        url = reverse("app-accounts:login")
        response = client.get(url)
        assert response.status_code == 200
        assert 'accounts/login.html' in [t.name for t in response.templates]