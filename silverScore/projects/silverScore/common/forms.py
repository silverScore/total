from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ExtendedUserForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ExtendedUserForm
        fields = ['username', 'password', 'email', 'phone', 'created_at']


class ChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = ExtendedUserForm
        fields = ['username', 'password', 'email', 'phone', 'created_at']


# class CreateUserForm(UserCreationForm):
#    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#    phone = forms.CharField(validators=[phone_regex], max_length=17)
#    class Meta:
#       model = User
#      fields = ['username', 'email', 'password1', 'password2', 'phone']

# class UserForm(UserCreationForm):
#     email = forms.EmailField(label="이메일")
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone = forms.CharField(validators=[phone_regex], max_length=17)

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2", "email")