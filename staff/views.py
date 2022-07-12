from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from students.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from .models import Staff


# Create your views here.

class StudentsListView(ListAPIView):
    """
    List of all the students taking a Lecturer's course
    """
    def get_queryset(self):
        lecturer = Staff.objects.get(user = self.request.user)
        students = lecturer.staff_course.student_set.all()
        return students

    serializer_class = StudentSerializer
