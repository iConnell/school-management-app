from rest_framework.serializers import ModelSerializer
from .models import CustomBaseUser


class userSerializer(ModelSerializer):
    class Meta:
        model = CustomBaseUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'other_names',
            'email',
            'gender',
            'dob',
        )