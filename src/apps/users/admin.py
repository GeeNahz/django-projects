from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Speaker


admin.site.register(User, UserAdmin)
admin.site.register(Speaker)
