from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from products.utils import save_product
from http import HTTPStatus as status

class ProductCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'products/product_create.html'
        )
    
    def post(self, request):
        product = save_product(request)
        return render(
            request,
            'products/product_create.html',
            {"product": product},
            status= status.CREATED
        )