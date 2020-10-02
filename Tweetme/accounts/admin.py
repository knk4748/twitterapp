from django.contrib import admin

# Register your models here.
# admin.site.register(a)

from .models import UserProfile

admin.site.register(UserProfile)