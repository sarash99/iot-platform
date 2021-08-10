from django.db import models
from channel.models import Channel

# Create your models here.
class Feed(models.Model):
    feed_id = models.AutoField(primary_key=True, default=None)
    channel_id = models.ForeignKey(Channel, default=None, on_delete=models.CASCADE)
    field1 = models.FloatField( null=True)
    field1 = models.FloatField( null=True)
    field2 = models.FloatField(null=True)
    field3 = models.FloatField(null=True)
    field4 = models.FloatField(null=True)
    field5 = models.FloatField(null=True)
    field6 = models.FloatField(null=True)
    field7 = models.FloatField(null=True)
    field8 = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feed_id