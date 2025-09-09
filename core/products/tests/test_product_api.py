import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestProductAPI:

    # Product list API test
    def test_products_list_status_200(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("api-products:list")
        response = client.get(url)
        assert response.status_code == 200