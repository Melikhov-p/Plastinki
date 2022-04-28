from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Track, TrackType

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'author', 'title', 'price', 'track_type', 'published')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class TrackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackType
        fields = ('id', 'name')