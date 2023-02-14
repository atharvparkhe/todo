from time import strftime
from django.db import models
from app_base.models import BaseModel
from app_accounts.models import UserModel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .manager import *
from .utils import *
from datetime import timedelta


class TodoModel(BaseModel):
    user = models.ForeignKey(UserModel, related_name="todo_user", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    timings = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    objects = todoManager()
    admin_objects = models.Manager()
    def __str__(self):
        return self.title


class CategoryModel(BaseModel):
    user = models.ForeignKey(UserModel, related_name="category_user", on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    color_hex_code = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name


class EventModel(BaseModel):
    user = models.ForeignKey(UserModel, related_name="event_user", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    doc = models.FileField(upload_to="file", null=True, blank=True)
    category = models.OneToOneField(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True, validators=[date_time_valicator])
    finish = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(choices=status_choices, default=status_choices[0][1] ,max_length=15)
    expiered = models.BooleanField(default=False)
    members = models.ManyToManyField(UserModel)
    is_deleted = models.BooleanField(default=False)
    objects = eventManager()
    admin_objects = models.Manager()
    def __str__(self):
        return self.title

@receiver(pre_save, sender=EventModel)
def update_finish(sender, **kwargs):
    kwargs["instance"].finish = kwargs["instance"].start + timedelta(hours=1)