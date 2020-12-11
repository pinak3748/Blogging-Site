from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
  #  username = forms.CharField(max_length=20)
    email = forms.EmailField()
    # password1 = forms.CharField(max_length=20)
    # password2 = forms.CharField(max_length=20)

    class meta:
        model = User
        fields_order = ['username', 'email', 'password1', 'passport2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']