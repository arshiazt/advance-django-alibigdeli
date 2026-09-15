from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','title','content','status',
                  'created_date','published_date']