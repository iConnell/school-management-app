from django.urls import path
from .views import StudentDetailView, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# urlpatterns = [
#     path('<int:pk>/', StudentDetailView.as_view()),

# ]

router.register('', StudentViewSet, basename='studnet-views')

student_list = StudentViewSet.as_view({
    'get':'list',
})

student_detail = StudentViewSet.as_view({
    'get': 'retrieve', 'patch':'update'
})

urlpatterns = [
    path('', student_list, name='student-list'),
    path('<int:pk>/', student_detail, name='student-details')
]