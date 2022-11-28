from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def td_calendar(request):
    return render(request, 'td_calendar/td_calendar.html', context)
