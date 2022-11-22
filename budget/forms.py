from django import forms
from budget.models import BudgetEntry, BudgetCategory
from django.db import models
# from django.contrib.auth.models import User

def validate(value):
    # for (val in value):
    if (not value[0].isalpha()):
        raise forms.ValidationError("Please enter a whole number")


class BudgetEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.ModelChoiceField(queryset=BudgetCategory.objects.all())

    #new
    projected = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    actual = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    class Meta():
        model = BudgetEntry
        # fields = ('description', 'category')
        fields = ('description', 'category', 'projected', 'actual')
