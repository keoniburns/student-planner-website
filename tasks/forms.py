from django import forms
from tasks.models import TasksEntry
from django.db import models
# from django.contrib.auth.models import User


class TasksEntryForm(forms.ModelForm):
    assignment = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    course = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'Ex: 13:00 is 1pm'}))
    class Meta():
        model = TasksEntry
        fields = ('assignment','course','date','time')
        # fields = ('description', ['category'])
