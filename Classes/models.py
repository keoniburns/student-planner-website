from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ClassesCategory(models.Model):
    semester = models.CharField(max_length=128)

    def __str__(self):
        return self.semester


class ClassesEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    professor = models.CharField(max_length=60)
    units = models.CharField(max_length=2)
    semester = models.ForeignKey(ClassesCategory, on_delete=models.CASCADE)
    s_date = models.DateField()
    e_date = models.DateField()
    s_time = models.TimeField()
    e_time = models.TimeField()
    mon = models.BooleanField()
    tue = models.BooleanField()
    wed = models.BooleanField()
    thurs = models.BooleanField()
    fri = models.BooleanField()
