from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser 
        fields = ['username', 'password', 'email']

class UserSerializerLogin(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser 
        fields = ['username', 'email']