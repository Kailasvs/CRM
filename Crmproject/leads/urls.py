

from django.urls import path
from leads import views

urlpatterns = [
      path('',views.Home.as_view(),name=''),
]
        