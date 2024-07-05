from django.contrib.auth.models import User 
def custom_context(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        context['is_authenticated'] = True
        context['username'] = user.username
        context['gender'] = user.profile.gender  
        context['is_admin'] = user.is_superuser
        context['interests'] = user.profile.interests
        

    else:
        context['is_authenticated'] = False
        context['username'] = None
        context['gender'] =None
        context['is_admin'] = None
        context['interests'] = None
    
    return context
