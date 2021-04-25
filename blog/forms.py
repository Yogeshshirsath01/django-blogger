from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog


class RegsiterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog

        fields = (
            'title',
            'description',
        )
