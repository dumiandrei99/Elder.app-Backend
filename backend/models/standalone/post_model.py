import uuid
from django.db import models
from .user_model import User
from .group_model import Group


class Post(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False,
    )
    post_description = models.CharField(max_length = 350, null=True)
    post_group =  models.ForeignKey(
        Group,
        on_delete = models.CASCADE,
        related_name = 'post_groups',
        null=True
    )
    post_user =  models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        related_name = 'post_users',
        null=True
    )
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"