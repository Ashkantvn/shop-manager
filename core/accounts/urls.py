
from accounts.views import AppProfileView
from django.urls import path

app_name = 'app-accounts'

urlpatterns = [
    path('profile/', AppProfileView.as_view(), name='app-profile'),
]
