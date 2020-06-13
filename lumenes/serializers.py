from django.contrib.auth.models import User
from rest_framework import serializers

from lumenes.models import Video


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'url', 'upload_date')
