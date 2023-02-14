from django.contrib import admin
from .models import *

class TodoModelAdmin(admin.ModelAdmin):
    list_display = ["user", "is_completed"]

admin.site.register(TodoModel, TodoModelAdmin)