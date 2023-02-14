from django.db import models
from base.models import BaseModel
from authentication.models import UserModel

class TodoModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)