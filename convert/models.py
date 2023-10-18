from django.db import models
from datetime import datetime
# Create your models here.


class Instrument(models.Model):
    title = models.CharField(max_length=255, default="Nifty50")
    file = models.FileField(upload_to='template_data/', null=True, blank=True)
    start_time = models.TimeField(null = False, default = datetime.time(9,15,0))
    end_time = models.TimeField(null = False, default = datetime.time(15,30,0))
    category = models.CharField(max_length=255, default="Category")
    sub_category = models.CharField(max_length=255, default="Sub Category")
    is_active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    calculation_started = models.BooleanField(default=True)
    calculation_completed = models.BooleanField(default=True) 
    percentage = models.FloatField(default = 100,null=False)
    is_realtime = models.BooleanField(default=False)
    realtime_token = models.IntegerField(default = None,null=True,blank=True)
    is_future = models.BooleanField(default=False)
    expiry = models.DateField(null=True, blank=True)
    prev_day_close = models.FloatField(default = 100,null=False)


    def __str__(self):
        return self.title