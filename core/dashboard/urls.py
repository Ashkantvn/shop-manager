from django.urls import path
from dashboard.views import Test

app_name= "dashboard"

urlpatterns = [
    path("", Test.as_view(), name="test")
]