from django.db import models
# Create your models here.


class File(models.Model):
    title = models.CharField(max_length=255, default="Nifty50")
    file = models.FileField(upload_to='template_data/', null=True, blank=True)
    def __str__(self):
        return self.title