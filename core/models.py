from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (("M", "Male"), ("F", "Female"))


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)

    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
