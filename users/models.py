from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='avatars', blank=True, null=True, default='static/defaultuser.jpg')
