from django.urls import reverse
from rest_framework.views import status
from rest_framework.test import APITestCase, APIClient

from lumenes.models import Video
from lumenes.serializers import VideoSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_video(title="", url=""):
        if title != "" and url != "":
            Video.objects.create(title=title)

    def set_up(self):
        self.create_video("Plantas")
        self.create_video("TPJ")
        self.create_video("Vida en el desierto")
        self.create_video("Contactar siempre")


class GetAllVideosTest(BaseViewTest):

    def test_get_all_videos(self):
        """
        This test ensures that all videos added in the set_up method
        exist when we make a GET request to the videos/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("videos-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Video.objects.all()
        serialized = VideoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
