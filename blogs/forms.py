from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Post



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Enter Email Address',min_length=4, max_length=150)
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter password', min_length=7, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', min_length=7,widget=forms.PasswordInput)

    class meta:
        model=User
        fields=['username','email','password1','password2']

   

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class Loginform(AuthenticationForm):
     username = forms.CharField(label='Enter username',min_length=4, max_length=150)
     password = forms.CharField(label='Enter password', min_length=7, widget=forms.PasswordInput)

     class meta:
        model=User
        fields=['username','password']
