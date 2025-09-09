from django.shortcuts import render
from django.views import View
from products.models import Product

# Create your views here.
class ProductList(View):
    
    def get(self,request):
        products_list = Product.objects.all()
        return render(
            request,
            'products/list.html',
            context={
                "products":products_list
            }
        )