from django.urls import path
from products.views import ProductList

app_name = "template-products"


urlpatterns = [
    path("list/", ProductList.as_view(),name="list"),
]
