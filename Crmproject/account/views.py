from django.db import IntegrityError
from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class CountryViewset(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    http_method_names = ['get', 'post', 'put' , 'delete']
      
class StateViewset(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    http_method_names = ['get', 'post', 'put' , 'delete']