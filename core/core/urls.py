from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView 

urlpatterns = [
    # Redirect to login page
    path('', RedirectView.as_view(url=reverse_lazy('accounts:login'))),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
