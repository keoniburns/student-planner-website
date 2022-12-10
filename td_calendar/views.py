from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tasks.views import add
from tasks.forms import TasksEntryForm
from tasks.models import TasksEntry
from Classes.models import ClassesEntry
import json
from datetime import timedelta

# Create your views here.
# def valueToDict(_dict)


# function to take all of our entries and organize for the calendar
def maptodata(cal, entry):
    year = month = day = 0
    contents = {}

# for task entries
    if (entry.is_completed == False):
        year = entry.date.year
        month = entry.date.month
        day = entry.date.day

        text = f"{entry.course}: {entry.assignment}"

    # default vals
        start = f"{entry.time}"
        end = "10:00"
        print(start)
        contents = {"startTime": start, "endTime": end, "text": text}
    if year not in cal:
        cal[year] = {}
    if month not in cal[year]:
        cal[year][month] = {}
    if day not in cal[year][month]:
        cal[year][month][day] = []

    cal[year][month][day].append(contents)

    return cal


def mapClasses(cal, curDate, name):
    # for class entries
    year = curDate.year
    month = curDate.month
    day = curDate.day

    # ClassesEntry.s_date.
    text = f"{name}"
    contents = {"startTime": start, "endTime": end, "text": text}

    # making sure dates are initialzed in calendar dict
    if year not in cal:
        cal[year] = {}
    if month not in cal[year]:
        cal[year][month] = {}
    if day not in cal[year][month]:
        cal[year][month][day] = []

    cal[year][month][day].append(contents)

    return cal


@login_required(login_url='/login/')
def td_calendar(request):
    # cal = {}
    if (TasksEntry.objects.count != 0):
        all_task_entries = TasksEntry.objects.filter(user=request.user)
        for entry in all_task_entries:
            cal = maptodata(cal, entry)
    if (ClassesEntry.objects.count != 0):
        all_class_entries = ClassesEntry.objects.filter(user=request.user)
        for entry in all_class_entries:
            curDate = entry.s_date
            while curDate != entry.e_date:
                cal = mapClasses(cal, curDate, entry.name)
                curDate = curDate + timedelta(days=1)
    # context = {
    #     "cal": json.dumps(cal)
    # }

    return render(request, 'td_calendar/td_calendar.html')


def newEvent(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = TasksEntryForm(request.POST)
            if (add_form.is_valid()):
                # entry = add_form.cleaned_data["entry"]
                assignment = add_form.cleaned_data["assignment"]
                course = add_form.cleaned_data["course"]
                date = add_form.cleaned_data["date"]
                time = add_form.cleaned_data["time"]
                user = User.objects.get(id=request.user.id)
                # TasksEntry(user=user, description=description, entry=entry).save()
                TasksEntry(user=user, assignment=assignment,
                           course=course, date=date, time=time).save()
                return redirect("/td_calendar/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, "/td_calendar/", context)
        else:
            # Cancel
            return redirect("/td_calendar/")
    else:
        context = {
            "form_data": TasksEntryForm()
        }
    return render(request, 'tasks/add.html', context)
