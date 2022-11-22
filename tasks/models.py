from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
        ('school', 'Schools'),
        ('other', 'Others')
        ]
class TaskCategory(models.Model):
    category = models.CharField(max_length=128)
    # category = models.CharField(max_length=128, choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.category
class TasksEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
