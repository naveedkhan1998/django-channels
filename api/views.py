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
from rest_framework import status


@permission_classes([AllowAny])
class HealthView(APIView):
    def get(self,request,format=None):
        return Response({'message':'OK!'},status=status.HTTP_200_OK)