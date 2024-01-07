from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid



class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']  # Puedes agregar campos adicionales si es necesario

    def __str__(self):
        return self.email