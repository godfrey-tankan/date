from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .validator import ProfileManager

@login_required
def get_profile_data(request):
    user = request.user
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

    if request.method == 'POST':
        form_data = request.POST
        
        profile_manager = ProfileManager(user)
        updated_fields = profile_manager.get_updated_fields(form_data)

        if updated_fields:
            if user.username != form_data['first_name']:
                user.username = form_data['first_name']
                user.save()
            for field, value in updated_fields.items():
                setattr(profile, field, value)
            profile.save()
            return JsonResponse({'success': 'Profile updated successfully'})
        else:
            return JsonResponse({'success': 'No changes made to the profile'})

    profile_data = {
        'first_name': profile.first_name,
        'username': user.username,
        'last_name': profile.last_name,
        'email': user.email,
        'phone': profile.phone,
        'bio': profile.bio,
        'dob': profile.dob.isoformat() if profile.dob else None,
        'interests': profile.get_interests_display() if profile.interests else None,
        'gender': profile.get_gender_display() if profile.gender else None,
    }
    return JsonResponse(profile_data)