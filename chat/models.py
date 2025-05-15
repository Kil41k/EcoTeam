from users.models import User
from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  # для групповых чатов
    is_group = models.BooleanField(default=False)
    members = models.ManyToManyField(User)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
