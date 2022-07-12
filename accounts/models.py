from django.db import models
from django.contrib.auth.models import AbstractUser
import phonenumbers

# Create your models here.


USER_TYPES = (
    ('student', 'student'),
    ('staff', 'staff'),
    ('admin', 'admin')
)

GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

NEXT_OF_KIN_CHOICES = (
    ("father", "father"),
    ("mother", "mother"),
    ("brother", "brother"),
    ("sister", "sister"),
    ("guardian", "guardian"),
    ("other", "other"),
)


class CustomBaseUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class NextOfKin(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(CustomBaseUser, on_delete=models.CASCADE)
    kin_type = models.CharField(max_length=10, choices=NEXT_OF_KIN_CHOICES)
    email_address = models.EmailField()
    phone = phonenumbers.PhoneNumber(country_code=+234)
    address = models.CharField(max_length=200)