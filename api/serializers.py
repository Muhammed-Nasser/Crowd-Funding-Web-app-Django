from .serializers import *
from rest_framework import serializers
from projects.models import Projects, Categories, Images, Rating,Tags
from Users.models import Comment, Donation

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

     