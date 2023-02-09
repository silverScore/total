from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .forms import SignupForm, ChangeForm
from .models import ExtendedUserForm

class MyUserAdmin(UserAdmin):
    add_form = SignupForm
    form = ChangeForm
    model = ExtendedUserForm
    list_display = ['username', 'password', 'email', 'phone', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'created_at')}),
    )


admin.site.register(ExtendedUserForm, MyUserAdmin)