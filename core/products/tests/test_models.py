import pytest


@pytest.mark.django_db
class TestProductModels:
    def test_create_product_model(self, product):
        assert product.pk is not None
        assert product.product_name == "test"
        assert product.price == 100
        assert product.cost_price == 50
        assert product.expiry_date is not None
        assert product.quantity == 10
        assert product.supplier_number == "1234567890"
        assert product.create_date is not None
        assert product.update_date is not None

    def test_str_representation(self, product):
        assert str(product) == "test"
