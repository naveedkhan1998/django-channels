from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import get_resolver
from .serializers import EndpointSerializer

class EndpointListView(APIView):
    def get(self, request, format=None):
        # Get the default resolver for the project
        resolver = get_resolver()

        # Get all URL patterns from the resolver
        url_patterns = resolver.url_patterns

        # Extract endpoints from URL patterns
        endpoints = []

        def extract_endpoints(patterns, namespace=''):
            for pattern in patterns:
                if hasattr(pattern, 'url_patterns'):
                    print(pattern)
                    # For included namespaces, recursively extract endpoints
                    if namespace:
                        extract_endpoints(pattern.url_patterns, namespace + pattern.namespace + ':')
                elif hasattr(pattern, 'callback'):
                    print(pattern)
                    if namespace:
                    # For individual patterns, add the endpoint to the list
                        endpoints.append(namespace + pattern.callback.__module__ + '.' + pattern.callback.__name__)

        extract_endpoints(url_patterns)

        # Serialize the list of endpoints
        serializer = EndpointSerializer(data={'endpoints': endpoints})
        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)
