
from django.contrib import admin
from django.urls import path

# TODO: create 3 url's 1 for creating a tracking code , 1 for managing tracking code edit /delete /check results lastly for actually tracking,

from . import views
urlpatterns = [
    path('',views.show_form)
]
