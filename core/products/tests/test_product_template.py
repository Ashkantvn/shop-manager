import pytest
from django.urls import reverse
from products.tests.fixtures import product


@pytest.mark.django_db
class TestProductTemplate:

    # Product list template test
    def test_product_template_view(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("template-products:list")
        response = client.get(url)
        assert response.status_code == 200
        assert "products/list.html" in [
            template.name for template in response.templates
        ]

    def test_product_retrieve_template_veiw(
            self,
            authenticated_worker, product):
        client = authenticated_worker
        url = reverse(
            "template-products:retrieve",
            args=[product.product_slug]
        )
        response = client.get(url)
        assert response.status_code == 200
        assert "products/retrieve.html" in [
            template.name for template in response.templates
        ]

    def test_product_retrieve_template_view_not_found(
            self,
            authenticated_worker):
        client = authenticated_worker
        url = reverse("template-products:retrieve", args=["asdfjowjeflug"])
        response = client.get(url)
        assert response.status_code == 404
        assert "products/retrieve.html" in [
            template.name for template in response.templates
        ]
