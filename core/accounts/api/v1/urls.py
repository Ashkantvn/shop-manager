from django.urls import path 
from accounts.api.v1 import views
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'accounts'

urlpatterns = [
    path('profile/',views.UserProfileView.as_view(), name='profile'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update/<str:username>/', views.UserUpdateView.as_view(), name='update'),
]
