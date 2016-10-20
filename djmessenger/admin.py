from django.contrib import admin

from . import models


@admin.register(models.UserProfile)
@admin.register(models.ChatRoom)
@admin.register(models.Message)
class UserProfileAdmin(admin.ModelAdmin):
    pass
