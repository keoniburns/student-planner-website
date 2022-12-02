from django import forms
from django.db import models
from Classes.models import ClassesEntry, ClassesCategory
from django.core import validators
from django.contrib.auth.models import User

class ClassesEntryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    professor = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    units = forms.CharField(widget=forms.TextInput(attrs={'size': '20'}))
    semester = forms.ModelChoiceField(queryset=ClassesCategory.objects.all())
    s_date = forms.DateField(widget=forms.SelectDateWidget)
    e_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta():
        model = ClassesEntry
        fields = ('name', 'professor' ,'units', 'semester', 's_date', 'e_date')
