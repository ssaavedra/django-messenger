from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    profile_picture = models.ImageField(null=True, blank=True)
    last_online = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)


class ChatRoom(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    participants = models.ManyToManyField(UserProfile, related_name='chats')
    admins = models.ManyToManyField(
        UserProfile,
        related_name='admin_chats',
        blank=True,
    )

    def __str__(self):
        return 'Chat room for: {0}'.format(list(self.participants.all()))


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL)
    chat = models.ForeignKey(ChatRoom)
    timestamp = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return 'Message from {sender} at {timestamp}'.format(
            sender=self.sender,
            timestamp=self.timestamp,
        )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_saved_create_profile(sender, instance, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
