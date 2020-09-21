from .models import Character
from .models import ShadowAmp
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'STR', 'AGL', 'WILL', 'LOG', 'CHA', 'EDG']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ShadowAmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShadowAmp
        fields = ['name', 'description']
