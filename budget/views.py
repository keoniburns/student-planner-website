from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from budget.forms import BudgetEntryForm
from django.contrib.auth.models import User
from budget.models import BudgetEntry, BudgetCategory
from django.views.generic import View


# Create your views here.
@login_required(login_url='/login/')
def budget(request):
    if(BudgetCategory.objects.count() == 0):
        BudgetCategory(category = "Food").save()
        BudgetCategory(category = "Clothing").save()
        BudgetCategory(category = "Housing").save()
        BudgetCategory(category = "Education").save()
        BudgetCategory(category = "Entertainment").save()
        BudgetCategory(category = "Other").save()
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        BudgetEntry.objects.filter(id=id).delete()
        return redirect("/budget/")
    else:
        table_data = BudgetEntry.objects.filter(user=request.user)
    totActual = 0
    totProjected = 0

    
    for i in table_data:
        totActual += int(i.actual)
        totProjected += int(i.projected)
    comparison = totActual - totProjected

    
    
    context = {
        "comp": comparison, 
        "table_data": table_data
    }
    
    return render(request, 'budget/budget.html', context)

@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = BudgetEntryForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                # entry = add_form.cleaned_data["entry"]
                category = add_form.cleaned_data["category"]

                #new
                projected = add_form.cleaned_data["projected"]
                actual = add_form.cleaned_data["actual"]

                user = User.objects.get(id=request.user.id)
                # BudgetEntry(user=user, description=description, entry=entry).save()
                # BudgetEntry(user=user, description=description, category=category).save()
                BudgetEntry(user=user, description=description, category=category, projected=projected, actual=actual).save()
                return redirect("/budget/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'budget/add.html', context)
        else:
            # Cancel
            return redirect("/budget/")
    else:
        context = {
            "form_data": BudgetEntryForm()
        }
    return render(request, 'budget/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
        # Load Journal Entry Form with current model data.
        budgetEntry = BudgetEntry.objects.get(id=id)
        form = BudgetEntryForm(instance=budgetEntry)
        context = {"form_data": form}
        return render(request, 'budget/edit.html', context)
    elif (request.method == "POST"):
        # Process form submission
        if ("edit" in request.POST):
            form = BudgetEntryForm(request.POST)
            if (form.is_valid()):
                budgetEntry = form.save(commit=False)
                budgetEntry.user = request.user
                budgetEntry.id = id
                budgetEntry.save()
                return redirect("/budget/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'budget/add.html', context)
        else:
            #Cancel
            return redirect("/budget/")

def pie_chart(request):
    data = [1,3]

    return render(request, 'core/home.html', data) 
    # return JsonResponse(data)

