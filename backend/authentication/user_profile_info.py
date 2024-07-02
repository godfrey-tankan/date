from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def get_profile_data(request):
    print('user profile requested!')
    user = request.user
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

    profile_data = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': user.email,
        'phone': profile.phone,
        'bio': profile.bio,
        'dob': profile.dob.isoformat() if profile.dob else None,
        'interests': profile.get_interests_display() if profile.interests else None,
        'gender': profile.get_gender_display() if profile.gender else None,
    }

    return JsonResponse(profile_data)