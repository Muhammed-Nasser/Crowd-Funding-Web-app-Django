from rest_framework import serializers
from .serializers import *
from projects.models import Projects, Categories, Images, Rating,Tags
from Users.models import *
from .serializers import *
# import from models in the same folder "app"


# serializer for user profile details

"""
- view his own:
    * profile
    * projects
    * donations
    * edit all except email
    * delete after confirm
"""


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reportno
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    # to get the related donation linked to the user profile
    user_donation = DonationSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data




# Projects

class CategoriesSer(serializers.ModelSerializer):
   class Meta:
      model = Categories
      fields = ['category', 'id']

class TagsSer(serializers.ModelSerializer):
   class Meta:
      model = Tags
      fields = ['tags', 'id']


class ProjectSer(serializers.ModelSerializer):
   category = CategoriesSer(many=False)
   tags = TagsSer(many=True)
   # comments = CommentSer(many=True)

   class Meta:
      model = Projects
      fields = ('id','title', 'details', 'total_target', 'start_time', 'end_time',  'category', 'tags')

class ImageSer(serializers.ModelSerializer):
   class Meta:
      model = Images
      exclude= ['project_id']

class CommentSer(serializers.ModelSerializer):
   class Meta:
      model = Comment
      fields = '__all__'

class DonationSer(serializers.ModelSerializer):
      class Meta:
         model = Donation
         fields = '__all__'

class RatingSer(serializers.ModelSerializer):
      class Meta:
         model = Rating
         fields = '__all__'

     
