from . import views
from django.urls import path

urlpatterns = [
    #path("homepage/", views.homepage, name="posts_home"),
    path("", views.api_endpoints, name="api_endpoints"),
    path("post-list/", views.list_posts, name="list_posts"),
    path("post-detail/<str:pk>", views.post_detail, name="post-detail"),
    path("post-create/", views.post_create, name="post-create"),
    path("post-update/<str:pk>", views.post_update, name="post-update"),
    path("post-delete/<str:pk>", views.post_delete, name="post-delete"),
]
