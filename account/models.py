from django.db import models
from django.contrib.auth.models import AbstractUser

GENDERS = [(i, i) for i in ["male", "female"]]


class User(AbstractUser): ...


class Student(models.Model):
    date_of_birth = models.DateField()
    student = models.OneToOneField(User, models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDERS)
    level = models.ForeignKey("landing.level", models.CASCADE, null=True)
    session = models.ForeignKey("landing.session", models.CASCADE, null=True)
    department = models.ForeignKey("landing.department", models.CASCADE, null=True)


class Kin(models.Model):
    email = models.EmailField()
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    student = models.OneToOneField(User, models.CASCADE)
    relationship = models.CharField(max_length=50, default="")
