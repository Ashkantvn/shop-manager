from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("create/", views.ProductCreateView.as_view(), name="create"),
    path(
        "<slug:product_slug>/",
        views.ProductDetailView.as_view(),
        name="detail"
    ),
    path(
        "<slug:product_slug>/delete",
        views.ProductDeleteView.as_view(),
        name="delete"
    ),
]
