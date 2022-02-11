from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import namedtuple
import projects
from .serializers import ProjectSer,CommentSer
from projects.models import Projects
from Users.models import Comment
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import namedtuple
import projects
from .serializers import ProjectSer,CommentSer
from projects.models import Projects
from Users.models import Comment



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


# @api_view(['GET'])
# def profile_detail(request,pk):

@api_view(['GET'])
def api_list(request):
	api_urls = {
		'List':'/project/list/',
		'Detail View':'/project/detail/<str:pk>/',
		'Create':'/project/create/',
		'Update':'/project/update/<str:pk>/',
		'Delete':'/project/delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def projectList(request):

	projects = Projects.objects.all()
	Project = ProjectSer(projects, many=True)
	comments = Comment.objects.all()
	commentSer = CommentSer(comments, many=True)

	api_return = {
		'Project Details': Project.data,
		'Project Comments': commentSer.data
	}
	return Response(api_return)
