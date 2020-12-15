from django.http import JsonResponse
from requests.exceptions import HTTPError
import requests
import json


def fetch_ipdata(ip_addr="1.1.1.1"):
    if ip_addr == '127.0.0.1':
        return {}
    try:
        x = requests.get('http://ip-api.com/json/'+ip_addr)
        print(type(x.json()))
        return x.json()
    except HTTPError as http_err:
        return {}
    except Exception as err:
        return {}
