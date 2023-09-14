from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from posts.views import PostsAPIView, PostDetailAPIView


# To verify that endpoint resolves to the correct url
class ApiUrlsTest(SimpleTestCase):
    def test_get_all_posts_is_resolved(self):
        url = reverse("postAPIView")
        self.assertEquals(resolve(url).func.view_class, PostsAPIView)

    # python3 manage.py test posts.tests.test_post_api_url.ApiUrlsTest.test_get_single_post_is_resolved
    def test_get_single_post_is_resolved(self):
        url = reverse("postAPIDetailView", args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailAPIView)


# To verify that endpoints getAll and post return the expected response
class PostAPIViewTests(APITestCase):
    postsViewUrl = reverse("postAPIView")

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="somepassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def tearDown(self):
        pass

    def test_get_posts_is_authenticated(self):
        response = self.client.get(self.postsViewUrl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_endpoint(self):
        data = {"title": "Post 2", "content": "Post 2 content"}
        response = self.client.post("/post-api/postAPIView", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Post 2")


# To verify that endpoints getSingle, updateSingle, deleteSingle post return the expected response
class PostAPIDetailViewTests(APITestCase):
    postsViewUrl = reverse("postAPIView")
    postsDetailViewUrl = reverse("postAPIDetailView", args=[1])

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="somepassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        # Saving User
        data = {"title": "Post 100", "content": "Post 100 content"}
        response = self.client.post(self.postsViewUrl, data, format="json")

    # ./manage.py test posts.tests.test_post_api_url.PostAPIDetailViewTests.test_get_single_post_authenticated
    def test_get_single_post_authenticated(self):
        response = self.client.get(self.postsDetailViewUrl)
        print(f"Title is: {response.data['title']}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Post 100")

    # python3 manage.py test posts.tests.test_post_api_url.PostAPIDetailViewTests.test_get_single_put_authenticated
    def test_get_single_put_authenticated(self):
        getResponse = self.client.get(self.postsDetailViewUrl)
        print(f"Title is: {getResponse.data['title']}")
        getResponse.data["title"] = "Post 100(updated)"
        putResponse = self.client.put(
            self.postsViewUrl, getResponse.data, format="json"
        )
        putResponse = self.client.put(
            self.postsDetailViewUrl, getResponse.data, format="json"
        )
        print(f"Updated Title is: {putResponse.data['title']}")
        self.assertEqual(putResponse.data["title"], "Post 100(updated)")
