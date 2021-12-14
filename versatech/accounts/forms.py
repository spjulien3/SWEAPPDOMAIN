from datetime import  datetime as dt
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput, Select

from accounts.models import Account
from django.contrib.auth import authenticate
class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address.")
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    username = forms.CharField(widget=forms.HiddenInput, initial="123", empty_value="temp")
    class Meta:
        model = Account
        fields = ("email", "username","first_name", "last_name","date_of_birth","password1","password2")

class AccountAuthenticationForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username','password')
    
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid Login")

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email',)
    
    def clean_email(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email"%s"is already in use.' % account.email)