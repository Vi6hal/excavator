from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Tracker, Result
from .create_logger_api import create_logger     
from .additional_infoapi import fetch_ipdata
from .additional_infoapi import fetch_uadata

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
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', False) or request.META.get('REMOTE_ADDR')
        received_json_data=json.loads(request.body)
        try:
            received_json_data.update(fetch_ipdata(ip_address))
            received_json_data.update(fetch_uadata(received_json_data.get('ua')))
            curr=Tracker.objects.get(request_tracking_code=received_json_data['tracker'])
            tracker_id=Result.objects.create(tracker=curr,
            origin_ip=ip_address,
            origin_country=received_json_data.get('country'),
            timezone=received_json_data.get('tzof'),
            device_gpu=received_json_data.get('gpu'),
            user_os=received_json_data.get('OS'),
            user_state=received_json_data.get('regionName'),
            user_city=received_json_data.get('city'),
            user_language=received_json_data.get('language'),
            user_isp=received_json_data.get('isp'),
            user_ua=received_json_data.get('ua'),
            request_api_ip=received_json_data.get('query'),
            user_screensize=received_json_data.get('screen_size'),
            device_type=received_json_data.get('device_type'),
            os_info=received_json_data.get('os_info'),
            device_info=received_json_data.get('device_info'),
            touch_support=received_json_data.get('touch_support'),
            browser_info=received_json_data.get('browser_info'),
            )
        except ObjectDoesNotExist:
            return JsonResponse({"status":"not ok"})
            pass


        return JsonResponse({"status":"ok"})

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
            data_res=Result.objects.filter(tracker=curr.id)
            for data in data_res:
                dict_single={}
                dict_single["create_date"]=data.create_date
                dict_single["origin_ip"]=data.origin_ip
                dict_single["origin_country"]=data.origin_country
                dict_single["timezone"]=data.timezone
                dict_single["user_ua"]=data.user_ua
                dict_single["user_isp"]=data.user_isp
                dict_single["request_api_ip"]=data.request_api_ip
                dict_single["user_language"]=data.user_language
                dict_single["user_screensize"]=data.user_screensize
                dict_single["device_gpu"]=data.device_gpu
                dict_single["device_info"]=data.device_info
                dict_single["touch_support"]=data.touch_support
                dict_single["browser_info"]=data.browser_info
                dict_single["device_type"]=data.device_type
                dict_single["os_info"]=data.os_info
                result_dict.append(dict_single)
            return JsonResponse({'data':result_dict})
        except ObjectDoesNotExist:
            return JsonResponse({})
