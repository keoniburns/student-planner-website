from django.db import models
from django.contrib.auth.models import User


class TasksEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.CharField(max_length=128)
    course = models.CharField(max_length=128)
    date = models.DateField(help_text = "12/25/2022")
    is_completed = models.BooleanField(default=False)
