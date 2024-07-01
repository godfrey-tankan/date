from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser, UserProfile
from django.http import JsonResponse
from .serializers import *
from rest_framework import status
from datetime import datetime

class UserAuthenticationAPIView(View):
    print('hiten...')
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form_type = request.POST.get('form_type')

        if form_type == 'signup':
            return self.register(request)
        elif form_type == 'signin':
            return self.login(request)
        else:
            print('Invalid form submission')
            messages.error(request, 'Invalid form submission')
            return redirect('login')

    def register(self, request):
        user_form = CustomUserSerializer(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()

            # Check if a profile already exists for the user
            try:
                profile = UserProfile.objects.get(user=user)
                # Update existing profile if found
                profile.first_name = request.POST.get('first_name')
                profile.last_name = request.POST.get('last_name')
                profile.phone = request.POST.get('phone')
                profile.bio = request.POST.get('bio')
                profile.gender = request.POST.get('gender')
                profile.dob = datetime.now()  # Example for setting dob
                profile.interests = request.POST.get('interests')
                profile.save()
            except UserProfile.DoesNotExist:
                # Create a new profile if none exists
                profile_data = {
                    'user': user.id,
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'phone': request.POST.get('phone'),
                    'bio': request.POST.get('bio'),
                    'gender': request.POST.get('gender'),
                    'dob': datetime.now(),  # Example for setting dob
                    'interests': request.POST.get('interests'),
                }
                profile_form = UserProfileSerializer(data=profile_data)
                if profile_form.is_valid():
                    profile_form.save()
                else:
                    messages.error(request, 'Failed to create profile. Please check the form.')

            messages.success(request, 'Registration successful. Please login.')
            return JsonResponse({'success':'Registration successful. Please login'}, status=200)
        else:
            messages.error(request, 'Registration failed. Please check the form.')
            return JsonResponse({'error':'Registration failed. Please check the form'}, status=400)


    def login(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return JsonResponse({'success': 'Login successful'}, status=200)
        else:
            messages.error(request, 'Invalid credentials.')
            return  JsonResponse({'error': 'Invalid credentials'}, status=400)
