from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from django.contrib.auth.decorators import login_required
from tasks.models import TaskCategory, TasksEntry
from budget.models import BudgetCategory, BudgetEntry

# Create your views here.


def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = {"join_form": join_form}
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'core/join.html', page_data)


@login_required(login_url='/login/')
def home(request):

    userTask = TasksEntry.objects.filter(user=request.user)
    userBudget = BudgetEntry.objects.filter(user=request.user)

    incompTasks = len([z for z in userTask if z.is_completed == False])
    compTasks = len([w for w in userTask if w.is_completed == True])

    context = {
        "bud": userBudget,
        "complete": compTasks,
        "incomplete": incompTasks
    }

    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                # Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                    username, password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        # Nothing has been provided for username or password.
        return render(request, 'core/login.html', {"login_form": LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")
# this will have join login logout about ltr
