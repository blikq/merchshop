# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

import random

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20, 
        unique=True,
        help_text='Required. 20 characters or fewer. Letters, digits, and spaces only.',
        validators=[],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class VerifyEmail(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    pin = models.IntegerField(default=random.randint(1000, 9999))
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.verified)
