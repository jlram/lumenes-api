from datetime import datetime

from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    upload_date = models.DateField(default=datetime.now)
