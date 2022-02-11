from django.db import router
from django.urls import include, path
from django.urls import include, path
from rest_framework import routers

# router = routers.DefaultRouter()

#register your view set
# from .routers import *
from . import views


urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.api_list, name="api/overview"),
    path('project/list/', views.projectList, name="project/list"),
    
]