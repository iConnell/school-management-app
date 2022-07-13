from rest_framework.serializers import ModelSerializer
from accounts.serializers import userSerializer

from .models import Student


class StudentSerializer(ModelSerializer):
    user = userSerializer()
    class Meta:
        model = Student
        fields = "__all__"


class StudentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'admit_date':{'read_only': True},
            'admit_level':{'read_only': True},
            'current_level':{'read_only': True},
            'exyg':{'read_only': True},
            'courses':{'read_only': True},
        }