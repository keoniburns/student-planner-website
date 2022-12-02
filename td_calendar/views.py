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

# Create your views here.
# def valueToDict(_dict)


#function to take all of our entries and organize for the calendar
def maptodata (cal, entry):
    year = month = day = 0
    contents = {}

    # for task entries
    if (type(entry) is TasksEntry):
        if(entry.is_completed == False):
            year = entry.date.year
            month = entry.date.month
            day = entry.date.day

            text = f"{entry.course}: {entry.assignment}"

        #default vals
            start = "00:00"
            end = "24:00"

            contents = { "startTime":start, "endTime":end, "text":text }

    # for class entries
    elif(type(entry) is ClassesEntry):
        pass

    #making sure dates are initialzed in calendar dict
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
    cal = {}
    if(TasksEntry.objects.count != 0):
        all_task_entries = TasksEntry.objects.filter(user=request.user)
        for entry in all_task_entries:
            cal = maptodata(cal, entry)

    if(ClassesEntry.objects.count != 0):
        all_class_entries = ClassesEntry.objects.filter(user=request.user)
        for entry in all_class_entries:
            cal = maptodata(cal, entry)


    context = {
        "cal" : json.dumps(cal)
    }

    return render(request, 'td_calendar/td_calendar.html', context)


def newEvent(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = TasksEntryForm(request.POST)
            if (add_form.is_valid()):
                # entry = add_form.cleaned_data["entry"]
                assignment = add_form.cleaned_data["assignment"]
                course = add_form.cleaned_data["course"]
                date = add_form.cleaned_data["date"]
                user = User.objects.get(id=request.user.id)
                # TasksEntry(user=user, description=description, entry=entry).save()
                TasksEntry(user=user, assignment=assignment,
                           course=course, date=date).save()
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
