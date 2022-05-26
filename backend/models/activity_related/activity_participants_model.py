import uuid
from django.db import models
from ..standalone.user_model import User
from ..standalone.activity_model import Activity


class ActivityParticipants(models.Model):
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

    uuid_activity = models.ForeignKey(
        Activity,
        on_delete = models.CASCADE,
        related_name = 'uuid_activity'
    )

    activity_name = models.CharField(max_length = 100)

    participant_name = models.CharField(max_length = 100)
    
    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"