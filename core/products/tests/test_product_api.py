import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestProductAPI:

    def test_products_list_status_200(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("api-products:list")
        client.get(url)
        assert client.status_code == 200