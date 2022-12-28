from rest_framework import serializers
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'photo']


class UserProfileSeralizer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'age', 'salary', 'address']
