from django.contrib.auth.models import User 
def custom_context(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        context['is_authenticated'] = True
        context['username'] = user.username
        context['gender'] = user.profile.gender  
        context['access_level'] = user.profile.access_level  
    else:
        context['is_authenticated'] = True
        context['username'] = 'tnqn'
        context['gender'] = 'male'
        context['access_level'] = None
    
    return context
