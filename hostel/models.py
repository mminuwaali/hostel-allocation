from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Block(models.Model):
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey("landing.level", models.CASCADE, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name.title()


class Room(models.Model):
    single = models.BooleanField(default=False)
    block = models.ForeignKey(Block, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.block} - {'single' if self.single else 'double'}"


class Bed(models.Model):
    room = models.ForeignKey(Room, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room.block} - {self.room} - {self.id}"
