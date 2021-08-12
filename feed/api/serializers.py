from feed.models import Feed
from rest_framework import serializers


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['field1', 'field2', 'field3', 'field4',  'field5',  'field6', 'field7', 'field8', 'created_at']