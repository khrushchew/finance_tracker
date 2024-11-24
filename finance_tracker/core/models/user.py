from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.FileField(null=True, blank=True , verbose_name='Photo')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
