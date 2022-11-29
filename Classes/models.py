from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClassesCategory(models.Model):
    category = models.CharField(max_length=128)
    def __str__(self):
        return self.category

class ClassesEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    units = models.CharField(max_length=128)
    category = models.ForeignKey(ClassesCategory, on_delete=models.CASCADE)
    year = models.CharField(max_length=128)
