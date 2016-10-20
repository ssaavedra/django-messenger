from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


def default_view(request):
    # Return the React view
    context = {}
    return render(request, 'react_loader.html', context)


class UserViewSet(ModelViewSet):
    queryset = models.UserProfile.objects
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserProfileSerializer

    @list_route()
    def logout(self, request, **kwargs):
        logout(request)
        return Response({'status': 'ok'})

    @list_route(url_path='self')
    def myself(self, request, **kwargs):
        profile = self.get_queryset().get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class ChatRoomViewSet(ModelViewSet):
    queryset = models.ChatRoom.objects
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ChatRoomSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.ReadOnlyChatRoomSerializer
        else:
            return self.serializer_class

    def get_queryset_production(self):
        """
        (On a real-world application, we would only get the user's own chats.)
        """
        profile, _ = models.UserProfile.objects.get_or_create(user=self.request.user)
        return profile.chats

    def get_queryset(self):
        """
        Get the chats for the requested user (or all users)
        """
        queryset = self.queryset
        user_id = self.request.query_params.get('user_id', None)

        if user_id is not None:
            profile, _ = models.UserProfile.objects.get_or_create(user__pk=user_id)
            queryset = profile.chats

        return queryset


class MessageViewSet(ModelViewSet):
    queryset = models.Message.objects
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.MesssageSerializer

    def get_queryset(self):
        queryset = self.queryset
        chat_id = self.request.query_params.get('chat_id', None)
        from_id = self.request.query_params.get('from', None)

        if chat_id is not None:
            queryset = queryset.filter(chat__pk=chat_id)

        if from_id is not None:
            queryset = queryset.filter(pk__gt=from_id)

        return queryset
