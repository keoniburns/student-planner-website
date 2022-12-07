from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from Classes.forms import ClassesEntryForm
from Classes.models import ClassesEntry, ClassesCategory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

# def collapseData (header_data, entry):
#     # year = 0
#     # semester = ""
#     # info = {}
#     # semester = "pog"
#     # year = entry.s_date.year
#     # text = f"Course: {entry.name} | Professor: {entry.professor} | Units: {entry.units} | Dates attended: {entry.s_date} - {entry.e_date}"
#     # info = {"text": text}
#     #
#     # if semester not in cal:
#     #     header_data[semester] = {}
#     # if year not in cal[semester]:
#     #     header_data[semester][year] = []
#     #
#     # header_data[semester][year].append(info)
#
#     semMonth = " "
#     semMonth
#
#     return header_data

# Create your views here.
@login_required(login_url='/login/')
def Classes(request):
    header_data = ["Fall","Winter", "Spring", "Summer"]
    if(ClassesCategory.objects.count() == 0):
        ClassesCategory(semester = "Fall").save()
        ClassesCategory(semester = "Winter").save()
        ClassesCategory(semester = "Spring").save()
        ClassesCategory(semester = "Summer").save()

    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        ClassesEntry.objects.filter(id=id).delete()
        return redirect("/Classes/")
    else:
        table_data = ClassesEntry.objects.filter(user=request.user)
<<<<<<< HEAD
        # for entry in table_data:
        #     header_data = collapseData(header_data, entry)
=======

        

>>>>>>> 8646abcf6231777b4728c9b611edc2d04c0d85b7
        context = {
            "table_data": table_data,
            "header_data": header_data
        }


    return render(request, 'Classes/Classes.html', context)

@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = ClassesEntryForm(request.POST)
            if (add_form.is_valid()):
                user = User.objects.get(id=request.user.id)
                name = add_form.cleaned_data["name"]
                professor = add_form.cleaned_data["professor"]
                units = add_form.cleaned_data["units"]
                semester = add_form.cleaned_data["semester"]
                s_date = add_form.cleaned_data["s_date"]
                e_date = add_form.cleaned_data["e_date"]

                ClassesEntry(user=user, name=name, professor=professor, units=units, semester=semester, s_date=s_date, e_date=e_date).save()
                return redirect("/Classes/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'Classes/add.html', context)
        else:
            # Cancel
            return redirect("/Classes/")
    else:
        context = {
            "form_data": ClassesEntryForm()
        }
    return render(request, 'Classes/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
        classesEntry = ClassesEntry.objects.get(id=id)
        form = ClassesEntryForm(instance = classesEntry)
        context = {"form_data": form}
        return render(request, 'Classes/edit.html', context)
    elif (request.method == "POST"):
        # Process form submission
        if ("edit" in request.POST):
            form = ClassesEntryForm(request.POST)
            if (form.is_valid()):
                classesEntry = form.save(commit=False)
                classesEntry.user = request.user
                classesEntry.id = id
                classesEntry.save()
                return redirect("/Classes/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'Classes/add.html', context)
        else:
            #Cancel
            return redirect("/Classes/")


# def pie_chart(request):
#     data = [1,3]
#
#     return render(request, 'core/home.html', data)
    # return JsonResponse(data)
