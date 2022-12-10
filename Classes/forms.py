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
    s_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'Ex: 13:00 is 1pm'}))
    e_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'Ex: 15:00 is 3pm'}))
    mon = forms.BooleanField(required=False)
    tue = forms.BooleanField(required=False)
    wed = forms.BooleanField(required=False)
    thurs = forms.BooleanField(required=False)
    fri = forms.BooleanField(required=False)

    class Meta():
        model = ClassesEntry
        fields = ('name', 'professor' ,'units', 'semester', 's_date', 'e_date','s_time', 'e_time', 'mon', 'tue', 'wed', 'thurs', 'fri')
