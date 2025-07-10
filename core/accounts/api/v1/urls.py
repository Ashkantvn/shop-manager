from django.urls import path 
from accounts.api.v1 import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('profile/',views.UserProfileView.as_view(), name='profile'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path('update/<str:username>/', views.UserUpdateView.as_view(), name='update'),
]
