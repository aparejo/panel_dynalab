from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='viewer')

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Cambia el nombre relacionado
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set_permissions",  # Cambia el nombre relacionado
        blank=True,
    )

    def __str__(self):
        return self.username
