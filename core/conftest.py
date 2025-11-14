import pytest
from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()

@pytest.fixture
def super_user(db):
    user = User.objects.create_superuser(
        username='testuser',
        password='password'
    )
    yield user
    if user.pk:
        user.delete()

@pytest.fixture
def authenticated_client():
    client = Client()
    client.login(username='testuser', password='password')
    yield client
    # loged out user if still logged in
    if client.session.get('_auth_user_id'):
        client.logout()

