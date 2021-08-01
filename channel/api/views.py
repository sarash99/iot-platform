from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from channel.api.serializers import ChannelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from channel.models import Channel
from account.models import Account
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


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
    data['channels'] =JSONRenderer().render(serializer.data)
    return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_channel(request, slug):
    data={}
    account = request.user
    try:
        channel = Channel.objects.get(channel_name=slug)
        if channel.user_id != account:
            data['response'] = "you don't have permission to visit this channel"
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)
    except Channel.DoesNotExist:
        data['response'] = "this channel does not exists"
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    channel_serializer = ChannelSerializer(channel)
    return Response(channel_serializer.data)


@api_view(['DELETE',])
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