from django.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class UserForm(Form):
    username_validator = User.username_validator
    username = CharField(min_length=3, max_length=32, validators=[username_validator], widget=TextInput({'class': 'form-control'}))
    password = CharField(min_length=3, max_length=32, widget=PasswordInput({'class': 'form-control'}))
