from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser, UserProfile  # Adjust import as per your project
from .serializers import CustomUserSerializer, UserProfileSerializer, UserLoginSerializer  # Adjust import as per your project

from django.contrib.auth import get_user_model
from django.contrib import messages

# class UserAuthenticationAPIView(APIView):
#     def post(self, request):
#         if 'form_type' in request.data:
#             form_type = request.data['form_type']
#             if form_type == 'register':
#                 return self.register(request)
#             elif form_type == 'login':
#                 return self.login(request)
#             else:
#                 return Response({'error': 'Invalid form_type provided'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'form_type field is required'}, status=status.HTTP_400_BAD_REQUEST)

#     def register(self, request):
#         print('register data is...', request.data)
#         user_serializer = CustomUserSerializer(data=request.data)
#         profile_serializer = UserProfileSerializer(data=request.data)

#         if user_serializer.is_valid() and profile_serializer.is_valid():
#             user = user_serializer.save()
#             profile_serializer.save(user=user)
#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def login(self, request):
#         print('login data is...', request.data)
#         serializer = UserLoginSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

class UserAuthenticationAPIView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        print('posted data is...:','username',request.POST.get('username'),'password',request.POST.get('password'),'form_type',request.POST.get('form_type'))
        form_type = request.POST.get('form_type')
        if form_type == 'signup':
            return self.register(request)
        elif form_type == 'signin':
            return self.login(request)
        else:
            messages.error(request, 'Invalid form submission')
            return redirect('login')  

    def register(self, request):
        print('register func called...')
        user_form = CustomUserSerializer(request.POST)
        profile_form = UserProfileSerializer(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print('user registered...', user)
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')  
        else:
            print('registration failed...')
            messages.error(request, 'Registration failed. Please check the form.')
            return redirect('login')  
    
    def login(self, request):
        print('login called!')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('user logged in...', user)
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            print('login failed...')
            messages.error(request, 'Login failed. Invalid credentials.')
            return redirect('login')  


