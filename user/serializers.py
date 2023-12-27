from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import password_validation as validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_password(self, data):
            validators.validate_password(password=data, user=User)
            return data

    def create(self, data):
        user = User(
            username = data['username'],
            email = data['email']
        )
        user.set_password(data['password'])
        user.save()
        return user
    

class PostRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()