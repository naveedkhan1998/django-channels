from django.db import models

# Create your models here.


class EmailLink(models.Model):
    chat_url = models.URLField(max_length=255,null=False,blank=True)
    seller_email = models.EmailField(null=False,blank=False)
    def __str__(self):
        return self.chat_url