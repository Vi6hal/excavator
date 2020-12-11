from django.shortcuts import render,HttpResponse
from datetime import datetime

# TODO: add views based on the TODO url's , create form handler for tracker, create view for tracker (show results) create a json-based api to interact with JS data 


def show_form(request):
    return HttpResponse(datetime.now())