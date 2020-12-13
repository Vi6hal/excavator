from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Tracker, results
import uuid

# TODO: add views based on the TODO url's , create form handler for tracker, create view for tracker (show results) create a json-based api to interact with JS data 

def show_form(request,tckcode):
    data={}
    try:
        curr=Tracker.objects.get(request_tracking_code=tckcode)
        data['tracking_code']=curr.request_tracking_code
        data['url']=curr.origin_url
        return render(request,"tracker.html",data)
    except ObjectDoesNotExist:
        data['tracking_code']=False
        data['url']=False
        return render(request,"tracker.html",data)


def home(request):
    return render(request,"home.html")

@csrf_exempt
def record_data(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        try:
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', False) or request.META.get('REMOTE_ADDR')
            curr=Tracker.objects.get(request_tracking_code=received_json_data['tracker'])
            tracker_id=results.objects.create(tracker=curr,origin_ip=ip_address,origin_country=received_json_data['country'],timezone=received_json_data['tzof'],device_gpu=received_json_data['gpu']
            )
        except ObjectDoesNotExist:
            pass


        return JsonResponse({"status":"ok"})

def create_logger(request):
    if request.method == 'POST':
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', False) or request.META.get('REMOTE_ADDR')
        print(ip_address)
        url_req=request.POST.get('access_key',False)
        curr=Tracker.objects.create(req_ip=ip_address,origin_url=url_req,request_tracking_code=uuid.uuid4().hex[:6].upper(),request_managing_code=uuid.uuid4().hex[:6].upper())
        return JsonResponse(
            {
                'managing_code':curr.request_managing_code,
                'origin_url':curr.origin_url,
                'tracking_code':curr.request_tracking_code,
            })

def load_logger(request):
    if request.method == 'POST':
        url_req=request.POST.get('access_key',False)
        try:
            curr=Tracker.objects.get(request_managing_code=url_req)
            return JsonResponse(
                {
                    'managing_code':curr.request_managing_code,
                    'origin_url':curr.origin_url,
                    'tracking_code':curr.request_tracking_code,
                })
        except ObjectDoesNotExist:
            return JsonResponse({
                    'managing_code':False,
                    'origin_url':False,
                    'tracking_code':False,
                })
def load_results(request):
    if request.method == 'POST':
        url_req=request.POST.get('access_key',False)
        try:
            result_dict=[]
            curr=Tracker.objects.get(request_managing_code=url_req)
            data_res=results.objects.filter(tracker=curr.id)
            for data in data_res:
                dict_single={}
                dict_single["create_date"]=data.create_date
                dict_single["device_gpu"]=data.create_date
                dict_single["origin_ip"]=data.origin_ip
                dict_single["origin_country"]=data.origin_country
                dict_single["timezone"]=data.timezone
                dict_single["device_gpu"]=data.device_gpu
                result_dict.append(dict_single)
            
            print(result_dict)
            return JsonResponse({'data':result_dict})
        except ObjectDoesNotExist:
            return JsonResponse({
                    'managing_code':False,
                    'origin_url':False,
                    'tracking_code':False,
                })

