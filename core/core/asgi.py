import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import dashboard.router as dashboardRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                dashboardRouter.websocket_urlpatterns
            )
        )
    }
)