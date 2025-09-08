from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from products.models import Product
from products.api.v1.serializers import ProductListSerializer

class ProductListAPI(APIView):
    
    def get(self,request):
        products_list = Product.objects.all()
        serializer = ProductListSerializer(products_list,many=True)
        return Response(data=serializer.data)
