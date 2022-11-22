from django import forms
from tasks.models import TasksEntry, TaskCategory
from django.db import models
# from django.contrib.auth.models import User

class TasksEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())
    class Meta():
        model = TasksEntry
        fields = ('description', 'category')
        # fields = ('description', ['category'])
