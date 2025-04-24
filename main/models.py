from django.db import models
from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=90)

    def __str__(self):
        return self.title

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='projectss')
    image = models.ImageField(upload_to='projimages')
    is_completed = models.BooleanField(default=False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proj = models.ForeignKey(Projects, on_delete=models.CASCADE)
    text = models.TextField()