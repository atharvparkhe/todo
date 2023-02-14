from django.contrib import admin
from .models import EventModel, TodoModel


admin.site.register(EventModel)
admin.site.register(TodoModel)