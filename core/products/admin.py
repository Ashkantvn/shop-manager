from django.contrib import admin
from products.models import Product, Category, Supplier


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = (
        "product_slug",
        "created_at",
        "updated_at",
    )


admin.site.register(Product, ProductAdmin)


admin.site.register([Category, Supplier])
