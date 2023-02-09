from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignupForm, ChangeForm
from .models import ExtendUserForm

# Register your models here.

class MyUserAdmin(UserAdmin):
    add_form = SignupForm
    form = ChangeForm
    model = ExtendUserForm
    list_display = ['username', 'password', 'email', 'phone', 'date_joined']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone',)}),
    ) #this will allow to change these fields in admin module


admin.site.register(ExtendUserForm, MyUserAdmin)
