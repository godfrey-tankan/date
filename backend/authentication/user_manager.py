from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Please provide an email address!'))
        if not username:
            raise ValueError(_('Username is required!'))
        if not first_name:
            raise ValueError(_('Enter your first name!'))
        if not last_name:
            raise ValueError(_('Enter your last name!'))
        if not phone:
            raise ValueError(_('The Phone field must be set'))
        if not password:
            raise ValueError(_('Password is required!'))

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user