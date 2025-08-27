import pytest
from accounts.tests.fixtures import authenticated_manager
from django.urls import reverse
from django.test import TestCase

@pytest.mark.django_db
class TestAccountApp:
    def test_app_profile_view(self, authenticated_manager):
        client = authenticated_manager
        url = reverse("app-accounts:app-profile")
        response = client.get(url)
        assert response.status_code == 200
        assert 'accounts/profile.html' in [t.name for t in response.templates]