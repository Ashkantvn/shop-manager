from django.shortcuts import render
from django.views import View


# Create your views here.
class ProductsDashboard(View):

    def get(self, request):
        return render(request, "dashboard/test.html")
