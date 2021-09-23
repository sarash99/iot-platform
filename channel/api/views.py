from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from channel.api.serializers import ChannelSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_api_key.models import APIKey
from rest_framework import status
from channel.models import Channel
from feed.models import Feed
from feed.api.serializers import FeedSerializer
import math
from datetime import datetime


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createChannel(request):
    account = request.user
    channel = Channel(user_id=account)
    serializer = ChannelSerializer(channel, request.POST)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['channel_fields'] = serializer.data
        data['response'] = "channel successfully created"
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_channel_list(request):

    account = request.user
    channels = Channel.objects.filter(user_id=account)
    data = {}
    serializer = ChannelSerializer(channels, many=True)
    data['channels'] = serializer.data
    return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_channel(request, slug):
    data = {}
    account = request.user
    try:
        channel = Channel.objects.get(channel_name=slug)
        if channel.user_id != account:
            data['response'] = "you don't have permission to visit this channel"
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    except Channel.DoesNotExist:
        data['response'] = "this channel does not exists"
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    channel_serializer = ChannelSerializer(channel)
    data['channel'] = channel_serializer.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def deleteChannel(request, slug):
    data = {}
    account = request.user
    try:
        channel = Channel.objects.get(channel_name=slug)
        if account != channel.user_id:
            return Response({'response': "you don't have permission to delete this channel"}, status=status.HTTP_401_UNAUTHORIZED)
    except Channel.DoesNotExist:
        data['response'] = "this channel does not exists"
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    operation = channel.delete()
    if operation:
        data['response'] = "channel is successfully deleted "
        return Response(data, status=status.HTTP_200_OK)

    data['response'] = "delete failed"
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def create_API_KEY(request, slug):
    data = {}
    account = request.user
    try:
        channel = Channel.objects.get(channel_name=slug)
        if account != channel.user_id:
            return Response({'response': "you don't have permission to access this channel"}, status=status.HTTP_401_UNAUTHORIZED)
    except Channel.DoesNotExist:
        data['response'] = "this channel does not exists"
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    api_key, key = APIKey.objects.create_key(name="my-remote-service")
    channel.api_key = api_key
    channel.save()
    data['api-key'] = key
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes((AllowAny,))
def receive_data(request):
    key = request.META["HTTP_AUTHORIZATION"].split()[1]
    api_key = APIKey.objects.get_from_key(key)
    channel = Channel.objects.get(api_key=api_key)
    feed = Feed(channel_id=channel)
    feedSerializer = FeedSerializer(feed, request.POST)
    data = {}
    if feedSerializer.is_valid():
        feedSerializer.save(channel_id=channel)
        data['response'] = 'data received'
        data['feed'] = feedSerializer.data
        return Response(data, status=status.HTTP_200_OK)
    return Response(feedSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_page_feeds(request, slug, page):
    data = {}
    account = request.user
    try:
        channel = Channel.objects.get(channel_name=slug)
        if channel.user_id != account:
            data['response'] = "you don't have permission to visit this channel"
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    except Channel.DoesNotExist:
        data['response'] = "this channel does not exists"
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    feeds = Feed.objects.filter(channel_id=channel).order_by('-created_at')
    feed_serializer = FeedSerializer(feeds, many=True)
    count = math.ceil(len(feed_serializer.data)/10)
    data['count'] = count
    data['feeds'] = feed_serializer.data[(page-1)*10: page*10]
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_filtered_feeds(request, slug):
    data = {}
    account = request.user
    try:
        channel = Channel.objects.get(channel_name=slug)
        if channel.user_id != account:
            data['response'] = "you don't have permission to visit this channel"
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    except Channel.DoesNotExist:
        data['response'] = "this channel does not exists"
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    filter_datetime = request.GET.get('filter_datetime', '')
    if filter_datetime:
        created_at = datetime.strptime(filter_datetime, "%Y-%m-%d %H:%M")
        feeds = Feed.objects.filter(created_at__gte=created_at, channel_id=channel).order_by('-created_at')
        feed_serializer = FeedSerializer(feeds, many=True)
        data['feeds'] = feed_serializer.data
    else:
        feeds = Feed.objects.all().order_by('-created_at')
        feed_serializer = FeedSerializer(feeds, many=True)
        data['feeds'] = feed_serializer.data[0:10]
    return Response(data, status=status.HTTP_200_OK)