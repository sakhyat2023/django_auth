from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms


class UpdatePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(attrs={"class": "form-control py-2"}),
    )

    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "form-control py-2"}),
    )

    new_password2 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "form-control py-2"}),
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]


class ResetUserPassword(SetPasswordForm):
    
    class Meta:
        model = User
        fields = "__all__"
