from django.contrib import admin
from . import views 
# from . import login
from .login import UserAuthenticationAPIView
from django.urls import path, include

urlpatterns = [
    # path('verify/', views.verify_view, name='verify'),
     path('', UserAuthenticationAPIView.as_view(), name='login'),
    path('home/', views.home_view, name='home'),

]