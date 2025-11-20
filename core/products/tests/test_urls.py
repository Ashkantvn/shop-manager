from django.urls import reverse, resolve
from products import views
import pytest


@pytest.mark.django_db
class TestProductUrls:
    def test_product_list_urls(self):
        url = reverse("products:list")
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductListView

    def test_product_detail_urls(self):
        url = reverse("products:detail", args=["test"])
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductDetailView

    def test_product_create_urls(self):
        url = reverse("products:create")
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductCreateView

    def test_product_delete_urls(self):
        url = reverse("products:delete", args=["test"])
        view_class = resolve(url).func.view_class
        assert view_class == views.ProductDeleteView
