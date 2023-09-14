from . import views as api_views
from django.urls import path
from rest_framework.authtoken import views

# urlpatterns for the function based view implementation
# urlpatterns = [
#     #path("homepage/", views.homepage, name="posts_home"),
#     path("", views.api_endpoints, name="api_endpoints"),
#     path("post-list/", views.list_posts, name="list_posts"),
#     path("post-detail/<str:pk>", views.post_detail, name="post-detail"),
#     path("post-create/", views.post_create, name="post-create"),
#     path("post-update/<str:pk>", views.post_update, name="post-update"),
#     path("post-delete/<str:pk>", views.post_delete, name="post-delete"),
# ]

# urlpatterns for the class based view implementation
urlpatterns = [
    path(
        "", api_views.api_endpoints, name="api_endpoints"
    ),  # this maps to a function based view to return all the available endpoints
    path("postAPIView", api_views.PostsAPIView.as_view()),
    path("postDetailAPIView/<int:pk>", api_views.PostDetailAPIView.as_view()),
    path("get-auth-token/", views.obtain_auth_token),  # this view accepts post request
]
