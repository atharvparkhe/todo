from django.db import models
from base.models import *

class UserModel(BaseUser):
    otp = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.email