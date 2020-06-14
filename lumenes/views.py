from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from lumenes.models import Video
from lumenes.serializers import UserSerializer, VideoSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler for the videos
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
