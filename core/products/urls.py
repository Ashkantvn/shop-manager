from django.urls import path
from products import views

app_name = "template-products"


urlpatterns = [
    path("list/", views.ProductList.as_view(),name="list"),
    path("<str:product_slug>/", views.ProductRetrieve.as_view(), name="retrieve")
]
