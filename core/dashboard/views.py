from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class ProductDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "dashboard/product_dashboard.html")