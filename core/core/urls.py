from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView 
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # Redirect to login page
    path('', RedirectView.as_view(url=reverse_lazy('accounts:login'))),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        # media and static files serving in development
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
        path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    ]