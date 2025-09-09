import pytest
from products import models
from datetime import date

@pytest.fixture
def category():
    category_object = models.Category.objects.create(
        category_name = "Test category",
        description = "Test description"
    )
    yield category_object
    if category_object.pk:
        category_object.delete()

@pytest.fixture
def supplier():
    supplier_object = models.Supplier.objects.create(
        supplier_name = "Test supplier",
        phone = "09865498765",
    )
    yield supplier_object
    if supplier_object.pk:
        supplier_object.delete()

@pytest.fixture
def product():
    category_object = models.Category.objects.create(
        category_name = "Test category1",
        description = "Test description"
    )
    supplier_object = models.Supplier.objects.create(
        supplier_name = "Test supplier1",
        phone = "09865498765",
    )
    product_object = models.Product.objects.create(
        product_name = "Test product",
        brand = "Brand name",
        quantity = 135.6,
        price = 185.65,
        cost_price = 14.65,
        expire_date = date(2025,1,3),
        supplier = supplier_object,
        location = "Location"
    )
    
    product_object.category.add(category_object)
    
    yield product_object
    
    if product_object.pk:
        product_object.delete()
    if supplier_object.pk:
        supplier_object.delete()
    if category_object.pk:
        category_object.delete()
