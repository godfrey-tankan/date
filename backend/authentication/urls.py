from django.contrib import admin
from . import views 
from django.urls import path, include

urlpatterns = [
    path('verify/', views.verify_view, name='verify'),
]