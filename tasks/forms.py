from django import forms
from tasks.models import TasksEntry, TaskCategory
from django.db import models
# from django.contrib.auth.models import User


class TasksEntryForm(forms.ModelForm):
    task = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta():
        model = TasksEntry
        fields = ('task','description', 'category','date')
        # fields = ('description', ['category'])
