from django.contrib import admin
from .models import *
from django.contrib.gis import admin
# Register your models here.
class MyModelAdmin(admin.OSMGeoAdmin):
    fields=('point','user')

admin.site.register(Distance, MyModelAdmin)
