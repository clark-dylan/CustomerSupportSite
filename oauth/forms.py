from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(forms.ModelForm):
    full_name       = forms.CharField(max_length=40, label='', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    username        = forms.CharField(max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email           = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password        = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    field_order = ['full_name', 'username', 'email', 'password']

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'password')

class LoginForm(forms.ModelForm):
        username = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Username/Email'}))
        password        = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

        class Meta:
            model = User
            fields = ('username', 'password')

# class LoginForm(forms.ModelForm):
#     username        = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Username/Email'}))
#     password        = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#
#     field_order = ['username', 'password']
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
