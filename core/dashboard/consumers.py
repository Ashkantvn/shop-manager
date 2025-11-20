from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ProductConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        # Let only superusers or staff connect
        if user.is_authenticated and (user.is_superuser or user.is_staff):
            await self.channel_layer.group_add("admins", self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("admins", self.channel_name)

    async def product_change_notification(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    # action like "created" "deleted"
                    "action": event["action"],
                }
            )
        )
