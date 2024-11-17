from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from user.services import validate_phone_number


class UserManager(BaseUserManager):
    """ user model manager where email is the unique identifier
    for authentication instead of usernames."""
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model where email is the unique identifier
    and not username."""

    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=55)
    last_name = models.CharField('last name', max_length=55, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    gender = models.CharField('gender', max_length=55, blank=True, null=True, 
                              choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    birthday_date = models.DateField('birthday date', blank=True, null=True)
    region = models.CharField('region', max_length=55, blank=True, null=True, choices=[('kipr', 'Kipr'), ('turkish', 'Turkish')])
    phone = models.CharField('phone number', max_length=18, 
                             validators=[validate_phone_number])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone']

    def __str__(self):
        return self.email
