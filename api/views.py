# user profile
"""
- view his own:
    * profile
    * projects
    * donations
    * edit all except email
    * delete after confirm
"""
from rest_framework import viewsets

# The Queryset required => end point to allow operations on the model
from Users.models import *
# group all common behaviour into the class
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
#     # permission_classes = [permissions.IsAuthenticated]


#
# @api_view(['GET'])
# def profile_detail(request,pk):
