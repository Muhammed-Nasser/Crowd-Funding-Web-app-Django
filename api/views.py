from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# group all common behaviour into the class
from .serializers import *

# The Queryset required => end point to allow operations on the model

# user profile
"""
- view his own:
    * profile
    * projects
    * donations
    * edit all except email
    * delete after confirm
"""


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def user_profile(request):
    current_user = request.user
    # only one profile per user => get
    current_user_profile = Profile.objects.get(user=current_user)
    # many projects => filter
    current_user_projects = Projects.objects.filter(user_id=current_user)
    # many donations => filter
    current_user_donations = Donation.objects.filter(user_id=current_user)

    # overall user donation => Just in one line ^^
    d_sum = sum(
        map(
            lambda x: x['amount_of_money'],
            current_user_donations.values('amount_of_money')
        )
    )

    # Setting up serializers
    profile_serializer = UserProfileSerializer()
    project_serializer = ProjectSer(many=True)
    donation_serializer = DonationSerializer(many=True)
    data = profile_serializer.to_representation(current_user_profile)
    data['projects'] = project_serializer.to_representation(current_user_projects)
    data['total-donations'] = d_sum
    data['donations'] = donation_serializer.to_representation(current_user_donations)
    return Response(data)


@api_view(['GET'])
def api_list(request):
    api_urls = {
        'User Profile': {
            'View': '/myprofile'
        },
        'Projects': {
            'List': '/project/list/',
            'Detail View': '/project/detail/<str:pk>/',
            'Create': '/project/create/',
            'Update': '/project/update/<str:pk>/',
            'Delete': '/project/delete/<str:pk>/',
        }

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
