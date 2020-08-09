from .models import UserDetails,Photos
from django import forms
from django.forms import ModelForm



class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'subject', 'user_message')


class SearchForm:
    class Meta:
        model = Photos
        fields = ('img','img_category','img_desc','img_special')
