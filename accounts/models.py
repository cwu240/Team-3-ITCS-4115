
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None


    first_name = models.CharField(max_length=2000,null=True,blank=True)
    last_name = models.CharField(max_length=2000,null=True,blank=True)
    gender = models.CharField(max_length=2000,null=True,blank=True)
    phone_number = models.CharField(max_length=2000,null=True,blank=True)
    dob = models.DateField(null=True, blank = True)



    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email