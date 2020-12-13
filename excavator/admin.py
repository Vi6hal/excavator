from django.contrib import admin
from .models import Tracker,results
    # TODO: register models on admin, override default str to make things more redable
admin.site.register(Tracker)
admin.site.register(results)
