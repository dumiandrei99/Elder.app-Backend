import uuid
from django.db import models
from .user_model import User


class VerificationCode(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False
    )

    uuid_user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'usernames'
    )

    email = models.CharField(max_length = 100)

    verification_code = models.CharField(max_length = 6)

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"