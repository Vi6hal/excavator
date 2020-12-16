from django.db import models
from datetime import datetime
from django import utils
import uuid

class Tracker(models.Model):
    """
    Basic Model Structure store basic info of creator for data deletion
    TODO: Genrate a 6 digit sequence code for tracking id
    
    """
    req_ip = models.CharField(max_length=30)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin_url = models.URLField(max_length=500)
    request_tracking_code = models.CharField(max_length=30,blank=True)
    request_managing_code = models.CharField(max_length=30,blank=True)
    tracker_url = models.URLField(max_length=500,blank=True)

    def __str__(self): 
         return self.origin_url


class Result(models.Model):
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=utils.timezone.now, blank=True)
    origin_ip = models.CharField(max_length=30,blank=True,null=True)
    origin_country=models.CharField(max_length=150,blank=True,null=True)
    timezone=models.CharField(max_length=250,blank=True,null=True)
    device_gpu=models.CharField(max_length=250,blank=True,null=True)
    user_os=models.CharField(max_length=150,blank=True,null=True)
    user_state=models.CharField(max_length=150,blank=True,null=True)
    user_city=models.CharField(max_length=150,blank=True,null=True)
    user_language=models.CharField(max_length=150,blank=True,null=True)
    user_isp=models.CharField(max_length=150,blank=True,null=True)
    user_ua=models.CharField(max_length=350,blank=True,null=True)
    request_api_ip=models.CharField(max_length=150,blank=True,null=True)
    user_screensize=models.CharField(max_length=150,blank=True,null=True)
    device_type=models.CharField(max_length=150,blank=True,null=True)
    os_info=models.CharField(max_length=150,blank=True,null=True)
    device_info=models.CharField(max_length=150,blank=True,null=True)
    touch_support=models.CharField(max_length=50,blank=True,null=True)
    browser_info=models.CharField(max_length=150,blank=True,null=True)
    
