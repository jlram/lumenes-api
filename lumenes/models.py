from datetime import datetime

from django.db import models


class Video(models.Model):

    title = models.CharField(max_length=100, null=False, unique=True)
    url = models.URLField(max_length=200, null=False, unique=True)
    upload_date = models.DateField(default=datetime.now, null=False)

    def __str__(self):
        return self.title
