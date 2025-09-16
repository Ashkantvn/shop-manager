from rest_framework.serializers import SerializerMethodField, ModelSerializer
from products.models import Product


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "brand",
            "quantity",
            "price",
            "expire_date"
        ]


class ProductRetrieveSerializer(ModelSerializer):

    category = SerializerMethodField()
    supplier = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "brand",
            "category",
            "quantity",
            "cost_price",
            "supplier",
            "expire_date",
            "location",
        ]

    def get_category(self, obj):
        categories = obj.category.all()
        return [
            {"id": category.id, "category_name": category.category_name}
            for category in categories
        ]

    def get_supplier(self, obj):
        supplier = obj.supplier
        return {
            "id": supplier.id,
            "supplier_name": supplier.supplier_name,
            "phone": supplier.phone,
            "email": supplier.email,
        }
