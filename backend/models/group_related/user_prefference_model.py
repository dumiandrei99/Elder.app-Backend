import uuid
from django.db import models
from ..standalone.user_model import User
from ..standalone.prefference_model import Prefference


class UserPrefference(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False
    )

    uuid_user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'uuid_user'
    )

    uuid_prefference = models.ForeignKey(
        Prefference,
        on_delete = models.CASCADE,
        related_name = 'uuid_prefference'
    )

    prefference_name = models.CharField(max_length = 100)

    liked = models.BooleanField()

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"