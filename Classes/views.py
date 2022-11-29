from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from Classes.forms import ClassesEntryForm
from Classes.models import ClassesEntry, ClassesCategory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/login/')
def Classes(request):
    if(ClassesCategory.objects.count() == 0):
        ClassesCategory(category = "Fall").save()
        ClassesCategory(category = "Winter").save()
        ClassesCategory(category = "Spring").save()
        ClassesCategory(category = "Summer").save()

    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        ClassesEntry.objects.filter(id=id).delete()
        return redirect("/Classes/")
    else:
        table_data = ClassesEntry.objects.filter(user=request.user)
        context = {
            "table_data": table_data
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
                units = add_form.cleaned_data["units"]
                category = add_form.cleaned_data["category"]
                year = add_form.cleaned_data["year"]

                ClassesEntry(user=user, name=name, units=units, category=category, actual=actual).save()
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
        # Load Journal Entry Form with current model data.
        ClassesEntry = ClassesEntry.objects.get(id=id)
        form = ClassesEntryForm(instance = ClassesEntry)
        context = {"form_data": form}
        return render(request, 'Classes/edit.html', context)
    elif (request.method == "POST"):
        # Process form submission
        if ("edit" in request.POST):
            form = ClassesEntryForm(request.POST)
            if (form.is_valid()):
                ClassesEntry = form.save(commit=False)
                ClassesEntry.user = request.user
                ClassesEntry.id = id
                ClassesEntry.save()
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
