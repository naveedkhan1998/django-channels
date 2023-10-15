import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.retry_count = 0

        # Try to connect, with reconnection attempts
        while self.retry_count < 5:
            try:
                # Join room group
                await self.channel_layer.group_add(self.room_group_name, self.channel_name)

                await self.accept()
                return
            except Exception as e:
                # Handle disconnection exception, you can log it or do custom handling
                self.retry_count += 1
                await asyncio.sleep(1)  # Wait for 1 second before retrying

        # If we reach here, reconnection attempts have failed
        await self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Your receive and chat_message methods remain unchanged

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["sender"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'user': user}
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, 'user': user}))
