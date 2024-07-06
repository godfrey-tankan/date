from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser, UserProfile
from django.http import JsonResponse
from .serializers import *
from rest_framework import status
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from os.path import splitext, join
from uuid import uuid4

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
            return redirect('login')

    def register(self, request):
        user_form = CustomUserSerializer(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            try:
                profile = UserProfile.objects.get(user=user)
                profile.first_name = request.POST.get('first_name')
                profile.last_name = request.POST.get('last_name')
                profile.phone = request.POST.get('phone')
                profile.bio = request.POST.get('bio')
                profile.gender = request.POST.get('gender')
                profile.dob = datetime.now() 
                profile.interests = request.POST.get('interests')
                profile_picture = request.FILES.get('profile_picture')
                if request.FILES.get('profile_picture'):
                    extension = splitext(profile_picture.name)[1]
                    filename = f"{request.POST.get('first_name')}{extension}"
                    file_path = join('static', 'profile_pictures', filename)
                    fs = FileSystemStorage()
                    profile_picture_path = fs.save(file_path, profile_picture)
                    profile.profile_picture = profile_picture_path
                profile.save()
                return redirect('home')
            except UserProfile.DoesNotExist:
                profile_data = {
                    'user': user.id,
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'phone': request.POST.get('phone'),
                    'bio': request.POST.get('bio'),
                    'gender': request.POST.get('gender'),
                    'dob': datetime.now(), 
                    'interests': request.POST.get('interests'),
                }
                profile_form = UserProfileSerializer(data=profile_data)
                if profile_form.is_valid():
                    profile_form.save()
                    return redirect('home')
                else:
                    return JsonResponse({'error': 'Failed to create profile. Please check the form.'}, status=400)
        else:
            errors = dict(user_form.errors.items())
            return JsonResponse({'error': errors}, status=400)

    def login(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful.'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=400)
