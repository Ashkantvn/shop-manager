from django.shortcuts import render
from django.views import View
from products.models import Product
from http import HTTPStatus


# Create your views here.
class ProductList(View):

    def get(self, request):
        products_list = Product.objects.all()
        return render(
            request, "products/list.html", context={"products": products_list}
        )


class ProductRetrieve(View):

    def get(self, request, product_slug):
        target_product = Product.objects.filter(product_slug=product_slug)

        # Check if product is available
        if target_product.exists():
            target_product = target_product.first()
            return render(
                request,
                "products/retrieve.html",
                context={"product": target_product},
            )
        else:
            return render(
                request,
                "products/retrieve.html",
                context={"error": "Product not found."},
                status=HTTPStatus.NOT_FOUND,
            )
