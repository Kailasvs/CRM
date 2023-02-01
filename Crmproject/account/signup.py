from django.db import IntegrityError
from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView




class SalesApiView(ModelViewSet):
    queryset = Users.sales_objects.all()
    serializer_class = Users_serailizer
    http_method_names = ['get', 'post', 'put' , 'delete']
    
    
    def get_object(self):
        return super().get_object()
    def create(self, request, *args, **kwargs):
        serializers=Users_serailizer(data=request.data)
        if serializers.is_valid():
            serializers.save(is_sales=True)
            return Response({'success':'succesfully saved'},status=status.HTTP_200_OK)
        return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try :
            instance = self.get_object()
            serializer = Users_UpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except IntegrityError as e :
           return Response({'error':'Updation failed'},status=status.HTTP_400_BAD_REQUEST)
                
   

    

class AdminApiView(ModelViewSet):
    queryset = Users.admin_objects.all()
    serializer_class = Users_serailizer
    http_method_names = ['get', 'post', 'put' , 'delete']
    
    
    def get_object(self):
        return super().get_object()
    def create(self, request, *args, **kwargs):
        serializers=Users_serailizer(data=request.data)
        if serializers.is_valid():
            serializers.save(is_admin=True)
            return Response({'success':'succesfully saved'},status=status.HTTP_200_OK)
        return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try :
            instance = self.get_object()
            serializer = Users_UpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except IntegrityError as e :
           return Response({'error':'Updation failed'},status=status.HTTP_400_BAD_REQUEST)
    
      
class TelecallingApiView(ModelViewSet):
    queryset = Users.telecaller_objects.all()
    serializer_class = Users_serailizer
    http_method_names = ['get', 'post', 'put' , 'delete']
    
    
    def get_object(self):
        return super().get_object()
    
    def create(self, request, *args, **kwargs):
        serializers=Users_serailizer(data=request.data)
        if serializers.is_valid():
            serializers.save(is_telecallers=True)
            return Response({'success':'succesfully saved'},status=status.HTTP_200_OK)
        return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try :
            instance = self.get_object()
            serializer = Users_UpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except IntegrityError as e :
           return Response({'error':'Updation failed'},status=status.HTTP_400_BAD_REQUEST)
       
       
class ManagerApiView(ModelViewSet):
    queryset = Users.manager_objects.all()
    serializer_class = Users_serailizer
    http_method_names = ['get', 'post', 'put' , 'delete']
    
    
    def get_object(self):
        return super().get_object()
    
    def create(self, request, *args, **kwargs):
        serializers=Users_serailizer(data=request.data)
        if serializers.is_valid():
            serializers.save(is_manager=True)
            return Response({'success':'succesfully saved'},status=status.HTTP_200_OK)
        return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try :
            instance = self.get_object()
            serializer = Users_UpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except IntegrityError as e :
           return Response({'error':'Updation failed'},status=status.HTTP_400_BAD_REQUEST)
       
class OperationsApiView(ModelViewSet):
    queryset = Users.operation_objects.all()
    serializer_class = Users_serailizer
    http_method_names = ['get', 'post', 'put' , 'delete']
    
    
    def get_object(self):
        return super().get_object()
    
    def create(self, request, *args, **kwargs):
        serializers=Users_serailizer(data=request.data)
        if serializers.is_valid():
            serializers.save(is_manager=True)
            return Response({'success':'succesfully saved'},status=status.HTTP_200_OK)
        return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try :
            instance = self.get_object()
            serializer = Users_UpdateSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except IntegrityError as e :
           return Response({'error':'Updation failed'},status=status.HTTP_400_BAD_REQUEST)
