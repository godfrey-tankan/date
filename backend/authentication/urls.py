from django.contrib import admin
from . import views 
from . import user_profile_info
from .login import UserAuthenticationAPIView
from django.urls import path, include


urlpatterns = [
    # path('verify/', views.verify_view, name='verify'),
    path('', UserAuthenticationAPIView.as_view(), name='login'),
    path('home/', views.home_view, name='home'),
    path('profile/', user_profile_info.get_profile_data, name='profile'),


]