from datetime import date
from django.db import models
from accounts.models import CustomBaseUser
from core.models import Course

# Create your models here.


Level_CHOICES = (("1", "One"), ("2", "Two"), ("3", "Three"), ("4", "Four"), ("5", "Five"), ("6", "Six"))


class Student(models.Model):
    # Admittance
    # TODO: Automatically calculate current level and exyg
    user = models.OneToOneField(CustomBaseUser, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    admit_date = models.DateField(default=date.today)
    admit_level = models.CharField(max_length=1, choices=Level_CHOICES, default="1")
    current_level = models.CharField(max_length=1, choices=Level_CHOICES, default="1")
    # Expected year of graduation
    exyg = models.DateField(blank=True, null=True)

    def __str__(self):
        name = self.user.first_name + ' ' + self.user.last_name
        return name

