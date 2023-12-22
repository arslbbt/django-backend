from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        print("layer", self.channel_layer)
        async_to_sync(self.channel_layer.group_add)("programmers", self.channel_name)
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        print("Websocket Message Received:", event["text"])
        async_to_sync(self.channel_layer.group_send)(
            "programmers", {"type": "chat.message", "message": event["text"]}
        )

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        async_to_sync(self.channel_layer.group_discard)(
            "programmers", self.channel_name
        )
        raise StopConsumer()

    def chat_message(self, event):
        print("Event...,", event)
