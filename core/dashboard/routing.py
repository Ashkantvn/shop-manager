from django.urls import path
from dashboard import consumers


websocket_urlpatterns = [
    path('ws/notifications/', consumers.TestConsumer.as_asgi()),
]