from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', views.home_api, name="home_api"),
    path('contact_api/', views.contactform, name="contact")
]