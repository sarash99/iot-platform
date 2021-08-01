from channel.models import Channel
from rest_framework import serializers


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['channel_name', 'field1', 'field2', 'field3', 'field4',  'field5',  'field6', 'field7', 'field8']
