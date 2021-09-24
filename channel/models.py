from django.db import models
from account.models import Account
from rest_framework_api_key.models import APIKey


# Create your models here.
class Channel(models.Model):
    channel_name = models.CharField(max_length=100)
    channel_id = models.AutoField(primary_key=True,default=None)
    user_id = models.ForeignKey(Account , default=None, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=50 , null=True)
    field1 = models.CharField(max_length=50, null=True)
    field2 = models.CharField(max_length=50, null=True)
    field3 = models.CharField(max_length=50, null=True)
    field4 = models.CharField(max_length=50, null=True)
    field5 = models.CharField(max_length=50, null=True)
    field6 = models.CharField(max_length=50, null=True)
    field7 = models.CharField(max_length=50, null=True)
    field8 = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    api_key = models.ForeignKey(APIKey, default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.channel_name



