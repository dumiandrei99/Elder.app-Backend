import uuid
from django.db import models


class Group(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False
    )

    group_name = models.CharField(max_length = 100)

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"