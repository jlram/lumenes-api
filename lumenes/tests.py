from rest_framework.views import status
from rest_framework.test import APITestCase, APIClient

from lumenes.models import Video
from lumenes.serializers import VideoSerializer


class VideoViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_video(title="", url=""):
        if title != "" and url != "":
            Video.objects.create(title=title, url=url)

    def setUp(self):
        """
        Override the setup method for the tests. Create some videos in the DB
        :return:
        """
        base_url = "https://rotula.net/"
        self.create_video("Plantas", base_url + "plantas")
        self.create_video("TPJ", base_url + "tpj")
        self.create_video("Vida en el desierto", base_url + "vida_en_el_desierto")
        self.create_video("Contactar siempre", base_url + "contactar_siempre")

    def test_get_all_videos(self):
        """
        This test ensures that all videos added in the set_up method
        exist when we make a GET request to the videos/ endpoint
        """
        # Hit the API endpoint
        response = self.client.get("/videos/")
        # Fetch the data from db
        expected = Video.objects.all()
        serialized = VideoSerializer(expected, many=True)
        # Compare the API results with the data in the DB
        self.assertEqual(
            response.data, serialized.data,
            msg="The response from the API ('{0}') does not match the result from the DB ('{1}')".format(
                response.data, serialized.data
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
