from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^create-channel/$', views.create_channel, name="create-channel"),
]
