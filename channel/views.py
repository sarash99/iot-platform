from django.shortcuts import render
from channel.forms import ChannelCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def create_channel(request):
    if request.POST:
        form = ChannelCreationForm(request.POST)
        if form.is_valid():
            #save channel
            instance = form.save(commit=False)
            instance.user_id = request.user.user_id
            instance.save
            #return redirect

    else:
        form = ChannelCreationForm()

    #return render channelcreation form