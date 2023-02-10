from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ExtendUserForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

class SignupForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = ExtendUserForm
        fields = ['username', 'password1', 'password2', 'email', 'phone']


class ChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = ExtendUserForm
        fields = ['username', 'password', 'email', 'phone']