from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser, UserProfile
from .serializers import *

class UserAuthenticationAPIView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form_type = request.POST.get('form_type')

        if form_type == 'signup':
            return self.register(request)
        elif form_type == 'signin':
            return self.login(request)
        else:
            messages.error(request, 'Invalid form submission')
            return redirect('login')

    def register(self, request):
        print('form data:', request.POST)
        user_form = CustomUserSerializer(data=request.POST)
        profile_form = UserProfileSerializer(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('login')
            
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print('User and profile created successfully')
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
        else:
            print('Registration failed')
            messages.error(request, 'Registration failed. Please check the form.')
            return redirect('login')

    def login(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            print('Login successful')
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            print('Login failed')
            messages.error(request, 'Login failed. Invalid credentials.')
            return redirect('login')
