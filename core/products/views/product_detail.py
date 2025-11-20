from django.shortcuts import render, redirect
from django.views import View
from products.utils import get_product_or_render_404, save_product


class ProductDetailView(View):
    def get(self, request, product_slug):
        result, not_found = get_product_or_render_404(request, product_slug)
        if not_found:
            return result
        else:
            context = {
                'product': result
            }
            return render(request, "products/product_detail.html", context)     

    def post(self, request, product_slug):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return redirect("accounts:login")
        # Check if product exists
        result, not_found = get_product_or_render_404(request, product_slug)
        if not_found:
            return result
        # Set new data
        product = result
        product = save_product(request, product)
        return render(
            request,
            "products/product_detail.html",
            {"product": product}
        )