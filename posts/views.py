from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

from .models import Post
# Create your views here.

def homepage(request:HttpRequest):
  #response = {"message": "Hello Django Rest Framework"}
  return JsonResponse("Hello Django Rest Framework", safe=False)

def api_endpoints(request:HttpRequest):
  response = {"api_urls": "API End points"}
  return JsonResponse(data=response)