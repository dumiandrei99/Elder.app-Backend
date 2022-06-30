import uuid
from django.db import models
from .user_model import User
from .post_model import Post

class Like(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False,
    )

    post_uuid =  models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'post_uuids',
    )

    liked_by =  models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'liked_bys',
    )

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"