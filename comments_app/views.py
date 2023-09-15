from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets, status


# Create your views here.
class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        comments = Comment.objects.all()
        # comments = Comment.objects.all()
        # serializer = CommentSerializer(comments, many=True)
        serializer = CommentSerializer(instance=comments, many=True)
        # return Response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(data=serializer.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # pk=None means the default value of pk is None
    def retrieve(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CommentSerializer(
            data=request.data
        )  # If you don't write data= then error was shown when I hit the endpoint. Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        comment = Comment.objects.get(id=pk)  # get the specific post
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
