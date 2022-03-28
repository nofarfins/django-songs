import rest_framework.fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'
        depth = 1


class PerformanceSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = (('Amount_of_views',))
        depth = 0


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        depth = 0


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        depth = 0


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'first_name', 'last_name', 'email'
        depth = 0


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 0
