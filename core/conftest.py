import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from products import models

User = get_user_model()


@pytest.fixture
def super_user(db):
    user = User.objects.create_superuser(
        username="testuser",
        password="password"
    )
    yield user
    if user.pk:
        user.delete()


@pytest.fixture
def authenticated_client(super_user):
    client = Client()
    client.login(username="testuser", password="password")
    yield client
    # loged out user if still logged in
    if client.session.get("_auth_user_id"):
        client.logout()


@pytest.fixture
def product(db):
    product = models.Product.objects.create(
        product_name="test",
        price=100.00,
        cost_price=50.00,
        expiry_date="2025-12-31",
        quantity=10,
        supplier_number="1234567890",
    )
    yield product
    if product.pk:
        product.delete()
