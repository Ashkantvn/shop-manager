from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from products.models import Product
from products.api.v1.serializers import ProductListSerializer, ProductRetrieveSerializer

class ProductListAPI(APIView):
    
    def get(self,request):
        products_list = Product.objects.all()
        serializer = ProductListSerializer(products_list,many=True)
        return Response(data=serializer.data)

class ProductRetrieveAPI(APIView):
    
    def get(self, request, product_slug):
        target_product = Product.objects.filter(product_slug=product_slug)

        # Check if product is available
        if target_product.exists():
            target_product = target_product.first()
            serializer = ProductRetrieveSerializer(target_product)
            return Response(data=serializer.data)
        else:
            return Response(
                data={'detail':'Product not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )