import pytest
from django.urls import reverse ,resolve
from django.test import Client
from accounts import views

@pytest.mark.django_db
class TestUrls:

    def test_account_login_url_is_resolved(self):
        url = reverse('accounts:login')
        view_class = resolve(url).func.view_class
        assert view_class == views.LoginView

    def test_account_logout_url_is_resolved(self):
        url = reverse('accounts:logout')
        view_class = resolve(url).func.view_class
        assert view_class == views.LogoutView