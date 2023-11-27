from rest_framework import serializers

class EndpointSerializer(serializers.Serializer):
    endpoint = serializers.CharField()
