from statistics import mode
from django.db import models

class TodoModel(models.Model):
    task = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)