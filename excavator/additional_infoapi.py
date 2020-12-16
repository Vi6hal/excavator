from django.http import JsonResponse
from requests.exceptions import HTTPError
from user_agents import parse
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

def fetch_uadata(ua_string):
    user_agent =parse(ua_string)
    brand = "Other" if user_agent.device.brand == None else user_agent.device.brand
    model = "Unidentified" if user_agent.device.model == None else user_agent.device.model
    os_family = "Other" if user_agent.os.family == None else user_agent.os.family
    os_name = "Other" if user_agent.os.version_string == None else user_agent.os.version_string
    browser_name = "Other" if user_agent.browser.family == None else user_agent.browser.family
    browser_ver = "Other" if user_agent.browser.version_string == None else user_agent.browser.version_string
    touch_support = "No" if user_agent.is_touch_capable == False else "Yes"
    device_type =get_device_type(user_agent)

    return {
        'browser_info': browser_name+" V("+browser_ver+")",
        "device_info": brand+" "+model,
        "os_info":os_family+os_name,
        "touch_support":touch_support,
        "device_type":device_type
    }

def get_device_type(user_agent):
    if user_agent.is_mobile:
        return 'Mobile'
    elif user_agent.is_pc:
        return 'PC'
    elif user_agent.is_bot:
        return 'BOT'
    elif user_agent.is_tablet:
        return 'TABLET'
    else:
        return "OTHER"
