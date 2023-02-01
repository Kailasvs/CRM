

from django.urls import path,include
from leads.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'leads',GeneralInformationViewset)
router.register(r'category',BusinessCategoryViewset)
router.register(r'personal',Personal_Information_Viewset)
router.register(r'business',Business_Information_Viewset)



urlpatterns = [
     path('',include(router.urls))
]
        