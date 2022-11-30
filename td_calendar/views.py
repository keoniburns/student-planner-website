from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tasks.views import add
from tasks.forms import TasksEntryForm
from tasks.models import TasksEntry, TaskCategory

# Create your views here.


@login_required(login_url='/login/')
def td_calendar(request):
    return render(request, 'td_calendar/td_calendar.html')


def newEvent(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = TasksEntryForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                # entry = add_form.cleaned_data["entry"]
                category = add_form.cleaned_data["category"]
                user = User.objects.get(id=request.user.id)
                # TasksEntry(user=user, description=description, entry=entry).save()
                TasksEntry(user=user, description=description,
                           category=category).save()
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
