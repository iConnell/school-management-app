from re import I
from django.urls import path
from .views import StudentCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("/create/", StudentCreateView, "students")

urlpatterns = router.urls
