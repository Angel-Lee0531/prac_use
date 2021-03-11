from django.db import models
from django.utils import timezone


class Post(models.Model):
    content = models.CharField(max_length=100)
    sub_date = models.DateTimeField(default = timezone.now)
