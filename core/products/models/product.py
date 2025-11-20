from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    supplier_number = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    product_slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name
    