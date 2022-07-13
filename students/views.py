from requests import request
from core.models import Course
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class StudentDetailView(RetrieveUpdateAPIView):
    def get_queryset(self):
        queryset = Student.objects.filter(user=self.request.user)
        return queryset

    serializer_class = StudentSerializer
    

class StudentViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = Student.objects.filter(user=self.request.user)
        return queryset

    serializer_class = StudentSerializer