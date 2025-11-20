from django.views import View
from products import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from products.utils import get_product_or_render_404
from http import HTTPStatus as status


class ProductListView(View):
    def get(self, request):
        products = models.Product.objects.all().only(
            "id", "name", "expiry_date", "quantity"
        )
        return render(
            request,
            "products/product_list.html",
            {"products": products}
        )


class ProductDeleteView(LoginRequiredMixin, View):
    def get(self, request, product_slug):
        result, not_found = get_product_or_render_404(request, product_slug)
        if not_found:
            return result
        product = result
        return render(
            request,
            "products/product_delete.html",
            {"product": product},
            status=status.OK,
        )

    def post(self, request, product_slug):
        result, not_found = get_product_or_render_404(request, product_slug)
        if not_found:
            return result
        product = result
        product.delete()
        return render(
            request,
            "products/product_delete.html",
            {"product_slug": product_slug},
            status=status.NO_CONTENT,
        )
