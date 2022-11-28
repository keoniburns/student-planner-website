from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from calendar import HTMLCalendar
from datetime import datetime


def calendar(request):
    return render(request)
