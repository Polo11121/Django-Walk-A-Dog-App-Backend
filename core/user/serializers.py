from rest_framework import serializers

from core.user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'phone_number', 'is_trainer']
