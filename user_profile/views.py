from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UpdatePasswordForm, ResetUserPassword

# Create your views here.
def user_profile(request):
    user_info = {"username": request.user.username, "email": request.user.email}
    return render(request, "user_profile.html", {"user_info": user_info})

def update_password(request):
    if request.method == "POST":
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,"Password update successfully")
            return redirect("user_profile")
    else:
        form = UpdatePasswordForm(request.user)
    return render(request, "update_password.html", {"form": form})

def reset_password(request):
    if request.method == "POST":
        form = ResetUserPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["new_password1"])
            user.save()
            messages.success("Password reset successfully")
            return redirect("login")
    else:
        form = ResetUserPassword(request)
    return render(request, "reset_password.html", {"form": form})
