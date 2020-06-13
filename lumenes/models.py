from datetime import datetime

from django.db import models


BASE_URL = "https://rotula.net"


class Video(models.Model):

    # Title assigned to the video
    title = models.CharField(max_length=100, null=False)
    # URL related to the video
    url = models.URLField(default=BASE_URL, max_length=200, null=False, unique=True)
    # Date when the video was uploaded
    upload_date = models.DateField(default=datetime.now, null=False)

    def __str__(self):
        return self.title
