from django.contrib import admin
from . import views 
# from . import login
from .login import LoginView
from django.urls import path, include

urlpatterns = [
    # path('verify/', views.verify_view, name='verify'),
     path('', LoginView.as_view(), name='login'),
    path('home/', views.home_view, name='home'),

]