from django.db import models
from django.contrib.auth.models import user


class event(moels.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
