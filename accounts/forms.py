
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email','role')

class Loginform(forms.Form):
    email = forms.CharField(label="email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model=User
        fields=[
            'email',
            'password'
            
        ]