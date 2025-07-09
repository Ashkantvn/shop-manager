from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.api.v1.views import (
    UserLogoutView,
    UserUpdateView,
    UserProfileView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class TestUrls(SimpleTestCase):
    def test_user_profile_url_is_resolved(self):
        url = reverse("accounts:profile")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, UserProfileView)

    def test_user_login_url_is_resolved(self):
        url = reverse("accounts:login")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , TokenObtainPairView)

    def test_user_logout_url_is_resolved(self):
        url = reverse("accounts:logout")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , UserLogoutView)

    def test_user_update_url_is_resolved(self):
        url = reverse("accounts:update",args=["testuser"])
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , UserUpdateView)

    def test_token_refresh_url_is_resolved(self):
        url = reverse("accounts:refresh_token")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , TokenRefreshView)