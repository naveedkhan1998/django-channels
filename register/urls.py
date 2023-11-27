from django.urls import path
from .views import EndpointListView

urlpatterns = [
    # Your other URL patterns...
    path('', EndpointListView.as_view(), name='get_all_endpoints'),
]
