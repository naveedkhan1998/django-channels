# chat/urls.py
from django.urls import path

from .views import index,room,SendMessageToWebSocket


urlpatterns = [
    path("", index, name="index"),
    path("ws/<str:room_name>/", room, name="room"),
    path('send_message_to_websocket/<str:room_name>/', SendMessageToWebSocket.as_view(), name='send_message_to_websocket'),
]
