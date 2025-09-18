import pytest
from django.urls import reverse, resolve
from products.api.v1 import views
from products import views as TemplateViews


@pytest.mark.django_db
class TestProductUrls:

    # Product list URL tests
    def test_product_list_url_is_resolved(self):
        url = reverse("api-products:list")
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductListAPI

    def test_template_product_list_url_is_resolved(self):
        url = reverse("template-products:list")
        view_class = resolve(url).func.view_class
        assert view_class == TemplateViews.ProductList

    # Product retrieve URL tests
    def test_product_retrieve_url_is_resolved(self):
        url = reverse("api-products:retrieve", args=["product-slug"])
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductRetrieveAPI

    def test_template_product_retrieve_url_is_resolved(self):
        url = reverse("template-products:retrieve", args=["product-slug"])
        view_class = resolve(url).func.view_class
        assert view_class == TemplateViews.ProductRetrieve
