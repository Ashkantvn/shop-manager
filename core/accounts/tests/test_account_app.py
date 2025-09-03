import pytest
from accounts.tests.fixtures import authenticated_manager, custom_user,worker
from django.urls import reverse
from django.test import Client
from accounts import models


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
        assert response.url == reverse("app-accounts:app-profile")

        # Check if the user is logged in
        response = client.get(reverse("app-accounts:app-profile"))
        assert response.status_code == 200
        assert client.session['_auth_user_id'] == str(custom_user.pk)

    # Test for app User update view
    def test_GET_user_update_view(self,authenticated_manager):                
        client =authenticated_manager
        url = reverse('app-accounts:update',args=[authenticated_manager.user.user_slug])

        response = client.get(url)
        assert response.status_code == 200
        assert 'accounts/update.html' in [template.name for template in response.templates]

    def test_POST_user_update_view(self,worker):
        # Make authenticated manager who is same is worker's manager
        business_manager = worker.business_manager
        client = Client()
        client.force_login(business_manager.user)

        url = reverse('app-accounts:update',args=[worker.user.user_slug])
      
        # Working time data
        data = {
            'start_time': "09:00",
            'end_time': "17:00"
        }

        response = client.post(url,data=data)

        assert response.status_code == 201
        assert models.WorkingTime.objects.filter(business_worker=worker).exists()


