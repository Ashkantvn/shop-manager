from django.urls import path 
from accounts.api.v1 import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:username>/',views.UserProfileView.as_view(), name='profile'),
    path('sign-up/', views.UserCreateView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update/<str:username>/', views.UserUpdateView.as_view(), name='update'),
]
