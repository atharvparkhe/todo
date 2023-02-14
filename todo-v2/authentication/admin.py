from django.contrib import admin
from .models import *

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]

admin.site.register(UserModel, UserModelAdmin)
