from django.urls import path
from products.api.v1 import views

app_name = "api-products"


urlpatterns = [
    path("list/", views.ProductListAPI.as_view(), name="list"),
    path("<str:product_slug>/", views.ProductRetrieveAPI.as_view(), name="retrieve")
]
