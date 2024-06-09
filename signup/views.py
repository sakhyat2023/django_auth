from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpUserForm

# Create your views here.
def signup_page(request):
    form = SignUpUserForm()
    if request.method == "POST":
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect("login")
    return render(request, "signup.html", {"form": form})