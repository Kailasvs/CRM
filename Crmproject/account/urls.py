from django.urls  import path,include
from . views import *
from . signup import *
from . import login,signup
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
router=DefaultRouter()

router.register(r'sales',SalesApiView)
router.register(r'admin',AdminApiView)
router.register(r'tele',TelecallingApiView)
router.register(r'manager',ManagerApiView)
router.register(r'operations',OperationsApiView)
router.register(r'admin',AdminApiView)
router.register(r'country',CountryViewset)
router.register(r'state',StateViewset)


urlpatterns = [
    path('login/',login.UserLoginView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('',include(router.urls))
]
