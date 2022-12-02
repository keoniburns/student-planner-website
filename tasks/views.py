from multiprocessing.util import is_abstract_socket_namespace
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tasks.forms import TasksEntryForm
from django.contrib.auth.models import User
from tasks.models import TasksEntry
from Classes.models import ClassesEntry


# Create your views here.


@login_required(login_url='/login/')
def tasks(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        TasksEntry.objects.filter(id=id).delete()
        return redirect("/tasks/")
    else:
        table_data = TasksEntry.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'tasks/tasks.html', context)


@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = TasksEntryForm(request.POST)
            if (add_form.is_valid()):
                assignment = add_form.cleaned_data["assignment"]
                course = add_form.cleaned_data["course"]
                date = add_form.cleaned_data["date"]
                user = User.objects.get(id=request.user.id)
                # TasksEntry(user=user, description=description, entry=entry).save()
                TasksEntry(user=user, assignment=assignment, course=course, date = date).save()
                return redirect("/tasks/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'tasks/add.html', context)
        else:
            # Cancel
            return redirect("/tasks/")
    else:
        context = {
            "form_data": TasksEntryForm()
        }
    return render(request, 'tasks/add.html', context)


@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
        # Load Journal Entry Form with current model data.
        tasksEntry = TasksEntry.objects.get(id=id)
        form = TasksEntryForm(instance=tasksEntry)
        context = {"form_data": form}
        return render(request, 'tasks/edit.html', context)
    elif (request.method == "POST"):
        # Process form submission
        if ("edit" in request.POST):
            form = TasksEntryForm(request.POST)
            if (form.is_valid()):
                tasksEntry = form.save(commit=False)
                tasksEntry.user = request.user
                tasksEntry.id = id
                tasksEntry.save()
                return redirect("/tasks/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'tasks/add.html', context)
        else:
            # Cancel
            return redirect("/tasks/")


def toggle(request, id):
    if (request.method == "POST" and "YES" in request.POST):
        TasksEntry.objects.filter(
            user=request.user, id=id).update(is_completed=False)
        return redirect('/tasks/')
    elif (request.method == "POST" and "NO" in request.POST):
        TasksEntry.objects.filter(
            user=request.user, id=id).update(is_completed=True)
        return redirect('/tasks/')
