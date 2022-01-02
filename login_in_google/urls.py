from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from login_in_google import views

urlpatterns = [
    path('', views.index, name='google_login'),
    path('logout', views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="index.html")),
]