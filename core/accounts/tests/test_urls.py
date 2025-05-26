from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.api.v1.views import (
    UserCreateView,
    UserLoginView,
    UserLogoutView,
    UserUpdateView,
)


class TestUrls(SimpleTestCase):
    def test_user_create_url_is_resolved(self):
        url = reverse("accounts:create")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , UserCreateView)

    def test_user_login_url_is_resolved(self):
        url = reverse("accounts:login")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , UserLoginView)

    def test_user_logout_url_is_resolved(self):
        url = reverse("accounts:logout")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , UserLogoutView)

    def test_user_update_url_is_resolved(self):
        url = reverse("accounts:update")
        view_class = resolve(url).func.view_class
        self.assertEqual( view_class , UserUpdateView)