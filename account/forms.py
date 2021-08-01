from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):

    class Meta:
        # tell the Registration Form what the form needs to look like
        model = Account
        fields = ("email", "username", "password")


class AccountLoginForm(forms.ModelForm) :

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("invalid login")





