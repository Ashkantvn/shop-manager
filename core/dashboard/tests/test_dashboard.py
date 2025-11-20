import pytest
import json
from channels.testing import WebsocketCommunicator
from core.asgi import application
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

User = get_user_model()

@pytest.mark.asyncio
@pytest.mark.django_db
class TestDashboardWebSocket:
    async def test_websocket_connection(self):
        user = await sync_to_async(User.objects.create_superuser)(
            username="admin",
            password="adminpassword"
        )

        communicator = WebsocketCommunicator(application, "/ws/products/")
        communicator.scope["user"] = user

        # Connect with timeout to prevent hanging
        try:
            connected, _ = await communicator.connect()
            assert connected, "WebSocket connection failed."
        finally:
            await communicator.disconnect()

    async def test_websocket_failed(self):
        user = await sync_to_async(User.objects.create_user)(
            username="user",
            password="userpassword",
            is_staff=False,
            is_active=False,
        )

        communicator = WebsocketCommunicator(application, "/ws/products/")
        communicator.scope["user"] = user

        try:
            connected, _ = await communicator.connect()
            assert not connected, "WebSocket connection should have failed"
        finally:
            await communicator.disconnect()
