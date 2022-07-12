from django.db import models
from accounts.models import CustomBaseUser
from core.models import Course
from students.models import Student

# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(CustomBaseUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    staff_students = models.ManyToManyField(Student, blank=True)
    staff_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
