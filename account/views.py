from django.shortcuts import render,redirect
from django.contrib.auth import login , authenticate,logout
from account.forms import RegistrationForm,AccountLoginForm


# Create your views here.
def registration_view(request):

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get("password")
            account = authenticate(email=email , password=raw_password)
            login(request, account)
            #return redirect to accounts page
        else:
            context['registration_form'] = form
    else: #GET request 
        form = RegistrationForm()
        context['registration_form'] = form
    #return render sigup form page


def logout_view(request):
    if request.POST:
        logout(request)
        #return redirect to homepage


def login_view(request):
    context = {}

    user = request.user
    #return user to account page if it's already authenticated
    if user.is_authenticated:
        #return redirect
        user = user #delete it
    if request.POST:
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email , password=password)

            if user: #if that user exists
                login(request , user)
                #return redirect account page

        else:
            form=AccountLoginForm()

        context['login_form'] = form
        #return render loginpage , context







