from rest_framework import serializers
from .models import *


class DistanceSerializer(serializers.Serializer):
    lat=serializers.DecimalField(max_digits=22,decimal_places=16)
    lon=serializers.DecimalField(max_digits=22,decimal_places=16)
