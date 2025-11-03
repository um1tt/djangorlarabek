from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser1(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username