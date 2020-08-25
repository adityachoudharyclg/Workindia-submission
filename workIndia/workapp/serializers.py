from rest_framework import serializers
from rest_framework import fields
from .models import PasswordManager

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=PasswordManager
        fields='__all__'