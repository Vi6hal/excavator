from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


# TODO: add views based on the TODO url's , create form handler for tracker, create view for tracker (show results) create a json-based api to interact with JS data 

def show_form(request):
    return render(request,"tracker.html")

@csrf_exempt
def record_data(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        return HttpResponse("OK")