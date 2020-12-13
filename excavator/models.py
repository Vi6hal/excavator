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




class results(models.Model):
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=utils.timezone.now, blank=True)
    origin_ip = models.CharField(max_length=30,blank=True)
    origin_country=models.CharField(max_length=30,blank=True)
    timezone=models.CharField(max_length=30,blank=True)
    device_gpu=models.CharField(max_length=30,blank=True)



