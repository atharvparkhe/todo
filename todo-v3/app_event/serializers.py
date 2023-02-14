from app_event.models import *
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    members = serializers.CharField(required=False)
    class Meta:
        model = EventModel
        exclude = ["is_deleted", "user"]

class EventDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        exclude = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        exclude = ["is_deleted"]

class TodoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        exclude = "__all__"

class InviteSerializer(serializers.Serializer):
    choice = serializers.CharField(required = True)


class AddMemberSerializer(serializers.Serializer):
    member_name = serializers.CharField(required = True)
    member_email = serializers.EmailField(required = True)