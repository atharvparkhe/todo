from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"