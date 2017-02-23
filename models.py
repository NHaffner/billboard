from django.db import models
from django.utils import timezone

class Post(models.Model):
    date = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=900)
    author = models.CharField(max_length=200)
