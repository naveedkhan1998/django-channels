# serializers.py
from rest_framework import serializers
from .models import EmailLink


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    user = serializers.CharField()


class EmailLinkSerializer(serializers.Serializer):
    class Meta:
        model = EmailLink
        fields = "__all__"
