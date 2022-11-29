from django import forms
from django.db import models
from Classes.models import ClassesEntry, ClassesCategory
from django.core import validators
from django.contrib.auth.models import User

class ClassesEntryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    units = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.ModelChoiceField(queryset=ClassesCategory.objects.all())
    year = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))

    class Meta():
        model = ClassesEntry
        fields = ('name', 'units', 'category', 'year')
