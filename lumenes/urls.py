from django.urls import path
from lumenes.views import ListVideosView


urlpatterns = [
    path('videos/', ListVideosView.as_view(), name="videos-all")
]
