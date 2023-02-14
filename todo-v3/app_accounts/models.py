from django.db import models
from app_base.models import BaseUser


class UserModel(BaseUser):
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    def __str__(self):
        return self.email
    class Meta:
        db_table = 'user'