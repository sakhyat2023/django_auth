from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.user_profile, name="user_profile"),
    path("update_password/", views.update_password, name="update_password"),
    path("reset_password/", views.reset_password, name="reset_password"),
]
