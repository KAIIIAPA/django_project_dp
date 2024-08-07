from rest_framework import serializers
from .models import NewsFilms
from django.contrib.auth.models import User

class NewsFilmsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsFilms
        fields = ('title', 'summary', 'description', 'created_at', 'img_url')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff',]
