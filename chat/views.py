# chat/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .serializers import EmailLinkSerializer
from rest_framework import status
from .utils import Util


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


@permission_classes([AllowAny])
class SendMessageToWebSocket(APIView):
    def get(self, request, room_name):
        message = request.query_params.get("message")
        user = request.query_params.get("user")

        if message is not None and user is not None:
            message_data = {
                "type": "chat_message",
                "message": message,
                "user": user,
            }
            channel_layer = get_channel_layer()

            # Send the message to the WebSocket consumer
            async_to_sync(channel_layer.group_send)(f"chat_{room_name}", message_data)

            return Response({"message": "Message sent to WebSocket."})
        return Response(
            {"error": "Both 'message' and 'user' parameters are required."}, status=400
        )


@permission_classes([AllowAny])
class EmailHandler(APIView):
    def get(self, request):
        chat_url = request.GET.get("chat_url")
        seller_email = request.GET.get("seller_email")

        if chat_url and seller_email:
            data = {
                "subject": "Chat Link",
                "body": f"Link to start Chat: {chat_url}",
                "to_email": seller_email,
            }
            Util.send_email(data)
            return Response({"message": "Email sent."}, status=200)
        else:
            return Response(
                {"error": "Missing required parameters {chat_url,seller_email}"},
                status=400,
            )
