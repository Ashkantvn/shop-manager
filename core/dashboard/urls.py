from django.urls import path
from dashboard.views import ProductsDashboard

app_name = "dashboard"

urlpatterns = [
    path("products/", ProductsDashboard.as_view(), name="products-dashboard"),
]
