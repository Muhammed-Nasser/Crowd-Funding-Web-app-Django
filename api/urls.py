from django.db import router
from django.urls import include, path
from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

#register your view set
from .routers import *



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('snippets/<int:pk>', views.snippet_detail),
    
]