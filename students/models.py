from datetime import date
from django.db import models
import phonenumbers

# Create your models here.


Level_CHOICES = (("1", "One"), ("2", "Two"), ("3", "Three"), ("4", "Four"), ("5", "Five"), ("6", "Six"))
NEXT_OF_KIN_CHOICES = (
    ("father", "father"),
    ("mother", "mother"),
    ("brother", "brother"),
    ("sister", "sister"),
    ("guardian", "guardian"),
    ("other", "other"),
)


class Student(models.Model):
    # Admittance
    # TODO: Automatically calculate current level and exyg
    admit_date = models.DateField(default=date.today)
    admit_level = models.CharField(max_length=1, choices=Level_CHOICES, default="1")
    current_level = models.CharField(max_length=1, choices=Level_CHOICES, default="1")
    # Expected year of graduation
    exyg = models.DateField()

    def __str__(self):
        name = self.first_name + self.last_name
        return name


class NextOfKin(models.Model):
    name = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=NEXT_OF_KIN_CHOICES)
    email_address = models.EmailField()
    phone = phonenumbers.PhoneNumber(country_code=+234)
    address = models.CharField(max_length=200)
