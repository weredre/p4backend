from django.shortcuts import render
from .models import Character
from .models import ShadowAmp
from authentication.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CharacterSerializer, UserSerializer, GroupSerializer,ShadowAmpSerializer


# Create your views here.
class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.AllowAny]  # Coule be [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShadowAmpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ShadowAmp.objects.all()
    serializer_class = ShadowAmpSerializer
    permission_classes = [permissions.IsAuthenticated]
