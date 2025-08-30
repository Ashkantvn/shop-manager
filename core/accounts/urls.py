
from accounts.views import AppProfileView, AppLoginView
from django.urls import path

app_name = 'app-accounts'

urlpatterns = [
    path('profile/', AppProfileView.as_view(), name='app-profile'),
    path('login/', AppLoginView.as_view(), name='login'),
]
