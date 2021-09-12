from feed.models import Feed
from rest_framework import serializers


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
