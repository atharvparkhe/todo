from django.db.models.fields import CharField
from rest_framework import serializers

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)

class signupSerializer(serializers.Serializer):
    name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)

# class verifySerializer(serializers.Serializer):

class resetSerializer(serializers.Serializer):
    npw = serializers.CharField(required = True)
    cpw = serializers.CharField(required = True)