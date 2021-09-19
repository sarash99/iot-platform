from django.urls import path
from channel.api import views

app_name = "channel"

urlpatterns = [
    path('create-channel/', views.createChannel),
    path('channel-list/', views.view_channel_list),
    path('<slug>/view-channel/', views.view_channel),
    path('<slug>/delete-channel/', views.deleteChannel),
    path('<slug>/create-api-key/', views.create_API_KEY),
    path('receive-data/', views.receive_data),
    path('<slug>/get-page-feeds/<int:page>/', views.view_page_feeds)
]