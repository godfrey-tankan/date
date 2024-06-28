from django.shortcuts import render

# Create your views here.

def verify_view(request):
    return render(request, 'verify.html')