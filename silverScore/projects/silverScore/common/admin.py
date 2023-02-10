from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import SignupForm, ChangeForm
from .models import ExtendUserForm

# Register your models here.

@admin.register(ExtendUserForm)
class MyUserAdmin(UserAdmin):
    add_form = SignupForm
    form = ChangeForm
    model = ExtendUserForm
    list_display = UserAdmin.list_display + ('username', 'password', 'email', 'phone', 'is_active', 'date_joined', 'last_login', 'updated_at')
    fieldsets = UserAdmin.fieldsets + ((_('Additional Fields'), {'fields': ('phone',)}),
    ) #this will allow to change these fields in admin module
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Fields'), {'fields': ('phone',)}),
    )

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)



# admin.site.register(ExtendUserForm, MyUserAdmin)
