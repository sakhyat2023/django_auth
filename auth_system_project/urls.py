from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('login/',include("login.urls")),
    path('signup/', include("signup.urls")),
    path('user/', include("user_profile.urls")),
]
