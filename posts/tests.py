from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class PostTests(TestCase):
    def test_create_post_endpoint(self):
        client = APIClient()
        response = client.post(
            "/post-api/postAPIView",
            {"title": "Post 2", "content": "Post 2 content"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post_endpoint(self):
        client = APIClient()
        data = {"title": "Post 2(Updated)", "content": "Post 2 content"}
        response = client.put("/post-api/postDetailAPIView/1", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create your tests here.
