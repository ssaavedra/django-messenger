from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
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
