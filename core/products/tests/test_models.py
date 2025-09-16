import pytest
from products.tests.fixtures import supplier, category, product
from products import models
from datetime import date


@pytest.mark.django_db
class TestProductsModels:

    # Check models are created
    def test_supplier_model_is_created(self, supplier):
        assert supplier.pk is not None

    def test_category_model_is_created(self, category):
        assert category.pk is not None

    def test_product_model_is_created(self, product):
        assert product.pk is not None

    # Check models fields
    def test_supplier_model_fields(self, supplier):
        assert supplier.supplier_name == "Test supplier"
        assert supplier.email == ""
        assert supplier.phone == "09865498765"

    def test_catrgory_model_fields(self, category):
        assert category.category_name == "Test category"
        assert category.description == "Test description"

    def test_product_model_fields(self, product):
        assert product.product_name == "Test product"
        assert isinstance(product.category.all()[0], models.Category)
        assert product.brand == "Brand name"
        assert product.quantity == 135.6
        assert product.expire_date == date(2025, 1, 3)
        assert isinstance(product.supplier, models.Supplier)
        assert product.location == "Location"

    # Check str method
    def test_supplier_str(self, supplier):
        assert str(supplier) == supplier.supplier_name

    def test_category_str(self, category):
        assert str(category) == category.category_name

    def test_product_str(self, product):
        assert str(product) == f"{product.product_name} by {product.brand}"
