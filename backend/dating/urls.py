from django.urls import path, include
from .views import *

urlpatterns = [
    path('',name='home', view=home_view),
    path('', include('authentication.urls')),
]
