from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.CharField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    date_of_birth = models.CharField(max_length = 255)
    is_first_login = models.BooleanField(default = True)

    REQUIRED_FIELDS = []

    class Meta:
        app_label = "backend"
