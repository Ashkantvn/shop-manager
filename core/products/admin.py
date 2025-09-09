from django.contrib import admin
from products.models import Product, Category, Supplier

# Register your models here.
admin.site.register([Product, Category, Supplier])