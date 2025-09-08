from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ManyToManyField("Category")
    brand = models.CharField(max_length=100)
    quantity = models.FloatField()
    price = models.FloatField()
    cost_price = models.FloatField()
    expire_date = models.DateField()
    supplier = models.ForeignKey(
        "Supplier",
        on_delete=models.SET_NULL,
        null=True
    )
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} by {self.brand}"