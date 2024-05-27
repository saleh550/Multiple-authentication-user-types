from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    TEACHER = 'teacher'
    STUDENT = 'student'
    VISITOR = 'visitor'

    ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (VISITOR, 'Visitor'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    average = models.FloatField()


class Visitor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add other visitor-specific fields here
