import pytest
from django.urls import reverse
from products.tests.fixtures import product


@pytest.mark.django_db
class TestProductAPI:

    # Product list API test
    def test_products_list_status_200(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("api-products:list")
        response = client.get(url)
        assert response.status_code == 200

    # Product retrieve API tests
    def test_product_retrieve_status_200(self, authenticated_worker, product):
        client = authenticated_worker
        url = reverse("api-products:retrieve", args=[product.product_slug])
        response = client.get(url)
        assert response.status_code == 200

    def test_product_retrieve_status_404(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("api-products:retrieve", args=["wrong-slug"])
        response = client.get(url)
        assert response.status_code == 404
