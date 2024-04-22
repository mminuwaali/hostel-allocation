from . import models
from django.contrib import admin


@admin.register(models.Block)
class BlockAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["block", "single"]
    list_display = ["single", "block", "created_at", "updated_at"]


@admin.register(models.Bed)
class BedAdmin(admin.ModelAdmin):
    list_filter = ["room"]
    search_fields = ["name"]
    list_display = ["room", "created_at", "updated_at"]
