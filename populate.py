# import django
import faker
# from staff.models import Staff
# from accounts.models import CustomBaseUser
# from students.models import Student
from faker import Faker
from faker.providers import profile

fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
# username = fake.username()



fak = fake.profile(fields=['username', 'name', 'mail'])
print(fak)

# django.setup()

#user = CustomBaseUser.objects.create()