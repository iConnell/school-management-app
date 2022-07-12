from django.db import models

# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    

    def __str__(self):
        return self.course_code
