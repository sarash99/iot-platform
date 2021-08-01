from django import forms
from channel.models import Channel

class ChannelCreationForm(forms.ModelForm):
    field1 = forms.CharField(max_length=50 , required=True)
    field2 = forms.CharField(max_length=50, required=False)
    field3 = forms.CharField(max_length=50, required=False)
    field4 = forms.CharField(max_length=50, required=False)
    field5 = forms.CharField(max_length=50, required=False)
    field6 = forms.CharField(max_length=50, required=False)
    field7 = forms.CharField(max_length=50 , required=False)
    field8 = forms.CharField(max_length=50 , required=False)


    class Meta:
        model = Channel
        fields = ['channel_name' , 'field1', 'field2', 'field3' ,'field4','field5','field6','field7','field8']

