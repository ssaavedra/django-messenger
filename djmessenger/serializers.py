

from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        depth = 0
        fields = ('id', 'username', 'first_name', 'last_name')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.UserProfile
        depth = 1


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChatRoom


class ReadOnlyChatRoomSerializer(serializers.ModelSerializer):
    participants = UserProfileSerializer(many=True)
    admins = UserProfileSerializer(many=True)

    class Meta:
        model = models.ChatRoom


class MesssageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        extra_kwargs = {
            'timestamp': {
                'read_only': True,
            },
        }
