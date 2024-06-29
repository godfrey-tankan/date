from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

# class LoginView(View):
#     def get(self, request):
#         return render(request, 'login.html')

#     def post(self, request):
#         print(request.user.is_authenticated, 'request body', request.body)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/') 
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid credentials'})

def login_view(request):
    if request.method == 'POST':
        print('request body', request.POST.get('username'), request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authentication logic goes here

        return JsonResponse({'message': 'Login successful'})  # Example response
    else:
        return render(request, 'login.html')  # Render login form template
    

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('request sent is...', request.POST.get('username'), request.POST.get('password'))
        
        # Process login form data (example: authenticate user)
        # Authentication logic goes here

        return JsonResponse({'message': 'Login successful'})