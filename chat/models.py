from users.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="send_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)