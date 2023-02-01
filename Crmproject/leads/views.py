from django.views import View
from rest_framework.viewsets import ModelViewSet
from . models import * 
from . serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.db  import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

# This class is used to create, update, delete and retrieve the General Information of the user
class GeneralInformationViewset(ModelViewSet):
    queryset = General_Information.objects.all()
    serializer_class = General_Information_serializer
    http_method_names = ['get', 'post', 'put' , 'delete']
    # A permission class that is used to check if the user is authenticated or not.
    permission_classes =[IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        serializers=General_Information_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save(created_by=request.user.id)
            return Response({'success':'succesfully saved'},status=status.HTTP_200_OK)
        return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
    

    
class BusinessCategoryViewset(ModelViewSet):
    queryset = Business_Category.objects.all()
    serializer_class = Business_Category_serializer
    http_method_names = ['get', 'post', 'put' , 'delete']
    
    
class Personal_Information_Viewset(ModelViewSet):
    queryset = Personal_Information.objects.all()
    serializer_class = Personal_Information_serializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'put' , 'delete']



class Business_Information_Viewset(ModelViewSet):
    queryset = Business_Information.objects.all()
    serializer_class = Business_Information_serializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'put' , 'delete']
        