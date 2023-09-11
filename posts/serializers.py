from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=50, blank=False, null=False)
  content = serializers.TextField(max_length=500)
  created = serializers.DateTimeField(auto_now_add=True)

  def create(self, validated_data):
    """
      Create and return a new `Post` instance, given the validated data.
    """
    return Post.objects.create(validated_data)
  
  def update(self, instance, validated_data):
    """
      Update and return an existing `Post` instance, given the validated data.
    """
    instance.title = validated_data.get('title', instance.title)
    instance.content = validated_data.get('content', instance.content)
    instance.save()
    return instance