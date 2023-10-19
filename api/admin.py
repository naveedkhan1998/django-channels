from typing import Any
from django.contrib import admin
from .models import Servers, Urls, ServiceEndpoints
from .helper import ping_websocket
# Register your models here.





class ServersAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Servers, form, change):
        if "is_active" in form.changed_data:
            qs_urls = Urls.objects.filter(server=obj)
            qs_endpoints = ServiceEndpoints.objects.filter(server=obj)
            
            if not obj.is_active:
                qs_urls.update(is_active=False)
                qs_endpoints.update(is_active=False)
            else:
                qs_urls.update(is_active=True)
                qs_endpoints.update(is_active=True)
            ping_websocket()

        obj.save()
        

class UrlsAdmin(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Urls, form: Any, change: Any) -> None:
        if "is_active" in form.changed_data:
            ping_websocket()
        obj.save()
        
class ServiceEndpointsAdmin(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Urls, form: Any, change: Any) -> None:
        if "is_active" in form.changed_data:
            ping_websocket()
        obj.save()
        


admin.site.register(Servers,ServersAdmin)
admin.site.register(Urls,UrlsAdmin)
admin.site.register(ServiceEndpoints,ServiceEndpointsAdmin)
