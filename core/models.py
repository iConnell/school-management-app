from django.db import models

# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    

    def __str__(self):
        return self.course_code


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=3)
    score = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.grade