from django.urls import path
from dashboard import views

urlpatterns = [
    path("products/", views.ProductDashboardView.as_view(), name="product_dashboard")
]
