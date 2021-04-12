from rest_framework import serializers
from .models import Post


class BlogSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=50)
    images=serializers.ImageField()
    description=serializers.CharField()
    category=serializers.CharField(max_length=20,default="")
    date = serializers.DateTimeField()

    class Meta:
        model=Post
        fields=['title','images','description','category','date']