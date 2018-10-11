from django.conf.urls import url, include
from .views import (
    TweetListAPIView,
    StreamAPI,
    CSVTweetListAPIView,
)

urlpatterns = [
    url(r'^stream/(?P<keyword>[\w-]+)/$', StreamAPI.as_view(), name='stream'),
    url(r'^search/$', TweetListAPIView.as_view() , name='search'),
    url(r'^csv/$', CSVTweetListAPIView.as_view() , name='csv'),
]
