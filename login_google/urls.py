from django.contrib import admin
from django.urls import path, include
from login_in_google import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_in_google.urls')),
]
