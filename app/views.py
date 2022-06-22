from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt, Radians
from django.db.models import F
from .serializers import *
from .models import *
import math
from math import sin, cos, sqrt, atan2, radians
# Create your views here.
import geopy.distance
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D

import math

def distance_to_decimal_degrees(distance, latitude):
    """
    Source of formulae information:
        1. https://en.wikipedia.org/wiki/Decimal_degrees
        2. http://www.movable-type.co.uk/scripts/latlong.html
    :param distance: an instance of `from django.contrib.gis.measure.Distance`
    :param latitude: y - coordinate of a point/location
    """
    lat_radians = latitude * (math.pi / 180)
    # 1 longitudinal degree at the equator equal 111,319.5m equiv to 111.32km
    return distance.m / (111_319.5 * math.cos(lat_radians))



class GetGeoLocationWithinDistance(APIView):
    def post(self,request):
       serializer=DistanceSerializer(data=request.data)
       if serializer.is_valid():
            try:
            #    print(serializer.data)

               data=serializer.data
               print(data)

               pnt=GEOSGeometry('point( {} {})'.format(data['lon'],data['lat']),srid=4326)
               print(pnt)

               location=Distance.objects.all()

               print(location)
               qs=Distance.objects.all().filter(point__distance_lte=(pnt,distance_to_decimal_degrees(D(km=2300),30.741482)))
               
               print(qs)
               
               return Response({'data':str(qs)})
            except Exception as e:
                print(e)
    #    else:
    #       serializer=DistanceSerializer(data=request.data)

    #       print('_______________')
       return Response({"msg":serializer.errors})           



# class DistanceAPI(APIView):

#     def post(self,request):

#         coords_1 = (19.076090, 72.877426)
#         coords_2 = (30.741482, 76.768066)
        
#         g=geopy.distance.geodesic(coords_1, coords_2).km
#         print(g)

#         return Response({"msg":g})

        # R = 6373.0

        # lat1 = radians(19.076090)
        # lon1 = radians(72.877426)

        # lat2 = radians(30.741482)
        # lon2 = radians(76.768066)
        
        # dlon = lon2 - lon1
        # dlat = lat2 - lat1
        
        # a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        # c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        # distance = R * c
        
        # return Response({"msg":distance})
        # print("Should be:", 278.546, "km")

        # R = 6373.0
        # # 76.728897
        # # 0.715490
        # lat1 =  float(request.data.get('lat'))
        # print(type(lat1))
        # lon1 =   float(request.data.get('lon'))

        # lat2=52.406374
    
        # lon2=16.9251681

        # dlon = lon2 - lon1
        # dlat = lat2 - lat1

        # a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        # c = 2 * atan2(sqrt(a), sqrt(1-a))
        # distance = R * c
        
        # print ("Result", distance)
        # print ("Should be", 278.546)
        # dlat = math.radians(lat2-current_lat1)
        # print(dlat)
        # dlon = math.radians(lon2-current_long1)
        # print(dlon)


        # a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(current_lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)

    
        # print(a)
        # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        # print(c)
        # d = 6371  * c
        # print(d)
   
        # LocationsNearMe = Distance.objects.annotate(distance=d).order_by('distance').filter(distance__lt=10)
        # print(LocationsNearMe)
    
        # return Response({"msg":distance})

        # dlat = Radians(F(lat) - current_lat1)
        # print(dlat)
        # dlong = Radians(F(lon) - current_long1) 
        # print(dlong)

        # a = (Power(Sin(dlat/2), 2) + Cos(Radians(current_lat1)) 
        # * Cos(Radians(F('lat'))) * Power(Sin(dlong/2), 2)
        # )
        # print(a)

        # c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
        # d = 6371 * c
        # print(d)

        # LocationsNearMe = Distance.objects.annotate(distance=d).order_by('distance').filter(distance__lt=10)
        # print(LocationsNearMe)

        # serializer=DistanceSerializer(data=request.data)

        # serializer.is_valid(raise_exception=True)

        # serializer.save()

        # return Response({"data":LocationsNearMe})





