from django.db import models


class Faculty(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(unique=True, max_length=100)


class Department(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(unique=True, max_length=100)
    faculty = models.ForeignKey(Faculty, models.CASCADE)


class Level(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(unique=True, max_length=40)


class Session(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(unique=True, max_length=40)
