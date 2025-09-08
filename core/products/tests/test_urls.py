import pytest
from django.urls import reverse, resolve
from products.api.v1 import views

@pytest.mark.django_db
class TestProductUrls:
    
    def test_products_list_url_is_resolved(self):
        url = reverse("api-products:list")
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductList