from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .user_manager import CustomUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime



class CustomUser(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, verbose_name=_('username'))
    email = models.EmailField(unique=True,max_length=100, verbose_name=_('email address'))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    
    def token(self):
        return self.token

class UserProfile(models.Model):
    gender_choices =[
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ]

    interests_choices = [
        ('love','love'),
        ('nostrings','nostrings'),
        ('hookups','hookups'),
        ('friendship','friendship'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    phone = models.CharField(max_length=15, verbose_name=_('phone number'))
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    interests = models.CharField(max_length=255, choices=interests_choices, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True)
    
    def __str__(self):
        return f"Profile of {self.user.username}"
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()