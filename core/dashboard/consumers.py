from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ProductConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("dashboard", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("dashboard", self.channel_name)

    async def product_updated(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "updated",
                    "product": event.get("product"),
                    "changes": event.get("message"),
                }
            )
        )

    async def product_created(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "created",
                    "message": event.get("message")
                }
            )
        )
