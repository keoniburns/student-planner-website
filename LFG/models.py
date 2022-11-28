from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
    ('Assignment help'),
    ('Study group'),
    ('Other')
    ]

class LFGCategory(models.Model):
    category = models.CharField(max_length=128)
    def __str__(self):
        return self.category

class LFGEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(LFGCategory, on_delete=models.CASCADE)
    assignment = models.CharField(max_length = 128)
    description = models.CharField(max_length = 256)
    location = models.CharField(max_length = 128)
    contact = models.CharField(max_length = 128)
