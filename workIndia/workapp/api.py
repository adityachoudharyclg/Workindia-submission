from rest_framework import serializers
from .models import PasswordManager
from rest_framework import viewsets,permissions
from .serializers import PasswordSerializer

# Password serializer
class PasswordViewSet(viewsets.ModelViewSet):
    queryset = PasswordManager.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class=PasswordSerializer