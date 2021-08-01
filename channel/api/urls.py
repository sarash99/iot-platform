from django.urls import path
from channel.api import views

app_name = "channel"

urlpatterns = [
    path('create-channel/', views.createChannel),
    path('channel-list/', views.view_channel_list),
    path('view-channel/<slug>/', views.view_channel),
    path('delete-channel/<slug>/', views.deleteChannel),
]