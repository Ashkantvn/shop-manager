from django.urls import reverse
from django.test import Client
from http import HTTPStatus as status
import pytest

@pytest.mark.django_db
class TestProductViews:
    def setup_method(self):
        self.client = Client()
        self.product_detail_url = reverse("products:detail", args=["test"])
        self.product_create_url = reverse("products:create")
        self.product_delete_url = reverse("products:delete", args=["test"])
        self.product_data ={
            "product_name": "Updated Product Name",
            "quantity": 10,
            "price": 20.5,
            "cost_price": 15.0,
            "expiry_date": "2024-12-31",
            "supplier_number": "1234567890"
        }

    # Product list test
    def test_GET_product_list_200(self):
        url = reverse("products:list")
        response = self.client.get(url)
        assert response.status_code == status.OK
        assert "products/product_list.html" in [
            template.name for template in response.templates
        ]

    # Product detail tests (get and Update)
    def test_GET_product_detail_200(self,product):
        response = self.client.get(self.product_detail_url)
        assert response.status_code == status.OK
        assert "products/product_detail.html" in [
            template.name for template in response.templates
        ]

    def test_GET_product_detail_404(self):
        response = self.client.get(self.product_detail_url)
        assert response.status_code == status.NOT_FOUND
        assert "products/product_detail.html" in [
            template.name for template in response.templates
        ]

    def test_POST_product_detail_200(self, product, authenticated_client):
        response = authenticated_client.post(
            self.product_detail_url,
            self.product_data
        )
        assert response.status_code == status.OK
        assert "products/product_detail.html" in [
            template.name for template in response.templates
        ]

    def test_POST_product_detail_302(self):
        response = self.client.post(
            self.product_detail_url,
            self.product_data
        )
        assert response.status_code == status.FOUND
        

    def test_POST_product_detail_404(self):
        response = self.client.post(
            self.product_detail_url,
            self.product_data
        )
        assert response.status_code == status.NOT_FOUND
        assert "products/product_detail.html" in [
            template.name for template in response.templates
        ]

    # Product creation tests
    def test_GET_product_creation_200(self, authenticated_client):
        response = authenticated_client.get(self.product_create_url)
        assert response.status_code == status.OK
        assert "products/product_create.html" in [
            template.name for template in response.templates
        ]

    def test_GET_product_creation_302(self):
        response = self.client.get(self.product_create_url)
        assert response.status_code == status.FOUND

    def test_POST_product_creation_201(self):
        response = self.client.post(self.product_create_url, self.product_data)
        assert response.status_code == status.CREATED
        assert "products/product_create.html" in [
            template.name for template in response.templates
        ]

    def test_POST_product_creation_302(self):
        response = self.client.post(self.product_create_url, self.product_data)
        assert response.status_code == status.FOUND

    # Product delete tests
    def test_GET_product_delete_200(self, product, authenticated_client):
        response = authenticated_client.get(self.product_delete_url)
        assert response.status_code == status.OK
        assert "products/product_delete.html" in [
            template.name for template in response.templates
        ]

    def test_GET_product_delete_302(self):
        response = self.client.get(self.product_delete_url)
        assert response.status_code == status.FOUND

    def test_GET_product_delete_404(self, authenticated_client):
        response = authenticated_client.get(self.product_delete_url)
        assert response.status_code == status.NOT_FOUND
        assert "products/product_delete.html" in [
            template.name for template in response.templates
        ]

    def test_POST_product_delete_204(self, product, authenticated_client):
        response = authenticated_client.post(self.product_delete_url)
        assert response.status_code == status.NO_CONTENT
        assert "products/product_delete.html" in [
            template.name for template in response.templates
        ]

    def test_POST_product_delete_302(self):
        response = self.client.post(self.product_delete_url)
        assert response.status_code == status.FOUND

    def test_POST_product_delete_404(self, authenticated_client):
        response = authenticated_client.post(self.product_delete_url)
        assert response.status_code == status.NOT_FOUND
        assert "products/product_delete.html" in [
            template.name for template in response.templates
        ]