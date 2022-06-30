import uuid
from django.db import models
from .user_model import User
from .post_model import Post


class Comment(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False,
    )

    comment = models.CharField(max_length = 350)

    post_uuid_comment =  models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'post_uuid_comments',
    )

    user_uuid_comment =  models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'user_uuid_comments',
    )

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"