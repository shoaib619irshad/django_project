from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, data):
        user = User(
            username = data['username'],
            email = data['email']
        )
        user.set_password(data['password'])
        user.save()
        return user