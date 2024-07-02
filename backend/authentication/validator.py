from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile

class ProfileManager:
    def __init__(self, user):
        self.user = user
        self.profile = user.profile

    def get_updated_fields(self, form_data):
        updated_fields = {}
        if 'first_name' in form_data and self.user.username != form_data['first_name']:
            updated_fields['first_name'] = form_data['first_name']

        if 'last_name' in form_data and self.profile.last_name != form_data['last_name']:
            updated_fields['last_name'] = form_data['last_name']

        if 'phone' in form_data and self.profile.phone != form_data['phone']:
            updated_fields['phone'] = form_data['phone']

        if 'bio' in form_data and self.profile.bio != form_data['bio']:
            updated_fields['bio'] = form_data['bio']

        if 'dob' in form_data and self.profile.dob != form_data['dob']:
            updated_fields['dob'] = form_data['dob']

        if 'interests' in form_data and self.profile.interests != form_data['interests']:
            updated_fields['interests'] = form_data['interests']

        if 'gender' in form_data and self.profile.gender != form_data['gender']:
            updated_fields['gender'] = form_data['gender']

        return updated_fields