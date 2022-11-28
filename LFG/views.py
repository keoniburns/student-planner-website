from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from LFG.forms import LFGEntryForm
from LFG.models import LFGEntry, LFGCategory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url='/login/')
def LFG(request):
    if(LFGCategory.objects.count() == 0):
            LFGCategory(category = "Assignment").save()
            LFGCategory(category = "Study Group").save()
            LFGCategory(category = "Tutoring").save()
            LFGCategory(category = "Extra Curricular").save()
            LFGCategory(category = "Other").save()

    if(request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        LFGEntry.objects.filter(id=id).delete()
        return redirect("/LFG/")
    else:
        table_data = LFGEntry.objects.filter(user=request.user)
        context = {
            "form_data": table_data
        }
    return render(request, 'LFG/LFG.html', context)


@login_required(login_url='/login/')
def add(request):
    if(request.method == "POST"):
        if("add" in request.POST):
            add_form = LFGEntryForm(request.POST)
            if (add_form.is_valid()):
                user = User.objects.get(id=request.user.id)
                category = add_form.cleaned_data["category"]
                assignment = add_form.cleaned_data["assignment"]
                description = add_form.cleaned_data["description"]
                location = add_form.cleaned_data["location"]
                contact = add_form.cleaned_data["contact"]

                LFGEntry(user=user, category=category, assignment=assignment, description=description, location=location, contact=contact).save()
                return redirect("/LFG/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'LFG/add.html', context)
        else:
            return redirect("/LFG/")
    else:
        context = {
            "form_data": LFGEntryForm()
        }
    return render(request, 'LFG/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
    if(request.method == "GET"):
        lfgEntry = LFGEntry.objects.get(id=id)
        form = LFGEntryForm(instance = lfgEntry)
        context = {
            "form_data": form
        }
        return render(request, 'LFG/edit.html',context)
    elif(request.method == "POST"):
        if("edit" in request.POST):
            form = LFGEntryForm(request.POST)
            if (form.is_valid()):
                lfgEntry = form.save(commit=False)
                lfgEntry.user = request.user
                lfgEntry.id = id
                lfgEntry.save()
                return redirect("/LFG/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'LFG/add.html', context)
        else:
            return redirect("/LFG/")
