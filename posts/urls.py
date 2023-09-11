from . import views
from django.urls import path

urlpatterns = [
    #path("homepage/", views.homepage, name="posts_home"),
    path("/post-api/", views.api_endpoints, name="api_endpoints"),
    #path("<int:post_index>", views.post_detail, name="post_detail"),
]
