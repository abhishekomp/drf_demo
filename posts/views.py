from django.shortcuts import render
from .serializers import PostSerializer
from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Post

# class based view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.


# Class based view
class PostsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = Post.objects.all()  # get the querySet
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)  # get the specific post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        # return Response({"message": "Item Deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Item Deleted"}, status=status.HTTP_204_NO_CONTENT)


# Function based view
def homepage(request: HttpRequest):
    # response = {"message": "Hello Django Rest Framework"}
    return JsonResponse("Hello Django Rest Framework", safe=False)


# This method returns the available endpoints for the api
# Function based view
@api_view(["GET"])
def api_endpoints(request: HttpRequest):
    api_urls = {
        "list_posts": "/post-list/",
        "post_detail": "/post-detail/<str:pk>/",
        "post-create": "/post-create/",
        "post-update": "/post-update/<str:pk>/",
        "post-delete": "/post-delete/<str:pk>/",
    }
    response = {"api_endpoints": api_urls}
    # return JsonResponse(data=response)
    return Response(
        api_urls
    )  # this is the response from the rest framework for a better view in the browser


# Using JsonResponse to return the serialized data. When using JsonResponse, then no need to use @api_view
# def list_posts(request):
#    if request.method == 'GET':
#       posts = Post.objects.all()  # get the querySet
#       serializer = PostSerializer(posts, many=True)
#       return JsonResponse(serializer.data, safe=False)

# Using Response class provided by Django Rest Framework
# @api_view(['GET'])
# def list_posts(request):
#    if request.method == 'GET':
#       posts = Post.objects.all()  # get the querySet
#       serializer = PostSerializer(posts, many=True)
#       return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def post_detail(request, pk):
#   post = Post.objects.get(id=pk)  # get the specific post
#   serializer = PostSerializer(post, many=False)
#   #return JsonResponse(serializer.data)
#   return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def post_create(request):
#   serializer = PostSerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#   return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["POST"])
# def post_update(request, pk):
#     post = Post.objects.get(id=pk)  # get the specific post
#     serializer = PostSerializer(instance=post, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(["DELETE"])
# def post_delete(request, pk):
#     post = Post.objects.get(id=pk)  # get the specific post
#     post.delete()
#     return Response("Delete successful", status=status.HTTP_200_OK)
