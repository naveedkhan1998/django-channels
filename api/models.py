from django.db import models
# Create your models here.

METHODS = {
    ('GET','GET'),
    ('POST','POST'),
    ('DELETE','DELETE'),
    ('PUT','PUT'),
}


class Servers(models.Model):
    title = models.CharField(max_length=255, default="FastAPI")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'Server Name:{self.title} |Is Active:{self.is_active} |'

class Urls(models.Model):
    server = models.ForeignKey(Servers,on_delete=models.CASCADE,blank=False,null=False)
    url = models.URLField(default="https://www.google.com/",unique=True,editable=True, max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'|Server:{self.server.title} |URL_ID:{self.id} |URL:{self.url} |Is Active:{self.is_active} |'
    
class ServiceEndpoints(models.Model):
    server = models.ForeignKey(Servers,on_delete=models.CASCADE,blank=False,null=False)
    method = models.CharField(choices=METHODS,blank=False,null=False)
    endpoint = models.CharField(default="",blank=False,null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'|Server:{self.server.title} |Method:{self.method} |Endpoint:{self.endpoint} |Is Active:{self.is_active} |'
    
