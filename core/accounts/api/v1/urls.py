from django.urls import path 
from accounts.api.v1 import views

app_name = 'accounts'

urlpatterns = [
    path('profile/',views.UserProfileView.as_view(), name='profile'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update/', views.UserUpdateView.as_view(), name='update'),
]
