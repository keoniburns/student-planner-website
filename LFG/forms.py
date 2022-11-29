from django import forms
from django.db import models
from LFG.models import LFGEntry, LFGCategory
from django.core import validators
from django.contrib.auth.models import User


class LFGEntryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=LFGCategory.objects.all())
    assignment = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))

    class Meta():
        model = LFGEntry
        fields = ('category','assignment','description','location','contact')
