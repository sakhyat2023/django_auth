from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginUserForm


# Create your views here.
def login_page(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("user_profile")
    else:
        form = LoginUserForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.warning(request, "User LogOut")
    return redirect("login")
