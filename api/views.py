from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import namedtuple
import projects
from .serializers import ProjectSer,CommentSer
from projects.models import Projects
from Users.models import Comment


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