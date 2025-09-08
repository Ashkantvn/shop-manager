from rest_framework.serializers import Serializer, ModelSerializer
from products.models import Product


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["id","product_name","brand","quantity", "price", "expire_date"]