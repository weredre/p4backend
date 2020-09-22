from .models import Character
from .models import ShadowAmp
from authentication.models import User
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'STR', 'AGL', 'WILL', 'LOG', 'CHA', 'EDG', 'ShadowAmp', 'user', 'id']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class ShadowAmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShadowAmp
        fields = ['name', 'description', 'id']
