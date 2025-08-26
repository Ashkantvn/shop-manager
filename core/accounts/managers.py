from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, pasword=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('first_name'):
            raise ValueError('Superuser must have a first name')
        if not extra_fields.get('last_name'):
            raise ValueError('Superuser must have a last name')
        if not username:
            raise ValueError('Superuser must have a username')

        return self._create_user(username, pasword, **extra_fields)