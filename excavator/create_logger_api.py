from django.http import JsonResponse
from .models import Tracker, Result
import uuid

def create_logger(request):
    if request.method == 'POST':
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', False) or request.META.get('REMOTE_ADDR')
        url_req=request.POST.get('access_key',False)
        curr=Tracker.objects.create(req_ip=ip_address,origin_url=url_req,request_tracking_code=uuid.uuid4().hex[:6].upper(),request_managing_code=uuid.uuid4().hex[:6].upper())
        return JsonResponse(
            {
                'managing_code':curr.request_managing_code,
                'origin_url':curr.origin_url,
                'tracking_code':curr.request_tracking_code,
            })