from . import models
from django.contrib import admin


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin): ...


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin): ...


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin): ...


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin): ...
