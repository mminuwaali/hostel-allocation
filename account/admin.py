from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin): ...


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin): ...


@admin.register(models.Kin)
class KinAdmin(admin.ModelAdmin): ...
