import uuid
from django.db import models
from ..standalone.user_model import User
from ..standalone.group_model import Group


class UserInGroup(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False
    )

    uuid_user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'uuid_user_group'
    )

    uuid_group = models.ForeignKey(
        Group,
        on_delete = models.CASCADE,
        related_name = 'uuid_prefference'
    )

    group_name = models.CharField(max_length = 100)

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"