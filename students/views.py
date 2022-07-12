from core.models import Course
from .models import Student
from .serializers import StudentSerializer


# Create your views here.


class RegisterCourses():
    class Meta:
        model = Course