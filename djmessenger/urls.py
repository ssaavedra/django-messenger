
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'user', views.UserViewSet)
router.register(r'chats', views.ChatRoomViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
        url(r'^api/', include(router.urls)),
        url(r'^', views.default_view),
]
