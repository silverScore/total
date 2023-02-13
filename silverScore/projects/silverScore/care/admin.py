from django.contrib import admin
from .models import Care, Address, Review
# Register your models here.

admin.site.register(Care)
admin.site.register(Address)
admin.site.register(Review)