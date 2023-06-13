from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, unique=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
