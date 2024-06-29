
# # custom_context_middleware.py

# from django.utils.deprecation import MiddlewareMixin
# from django.contrib.auth.models import User  

# class UserMiddlewareData(MiddlewareMixin):
#     def process_response(self, request, response):
#         if hasattr(request, 'user') and request.user.is_authenticated:
#             user = request.user
#             response.context_data['is_authenticated'] = True
#             response.context_data['username'] = user.username
#             response.context_data['gender'] = user.profile.gender  
#             response.context_data['access_level'] = user.profile.access_level 
#         else:
#             response.context_data['is_authenticated'] = False
#             response.context_data['username'] = None
#             response.context_data['gender'] = None
#             response.context_data['access_level'] = None
            
#         return response