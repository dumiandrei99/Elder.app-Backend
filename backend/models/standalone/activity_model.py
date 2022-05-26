import uuid
from django.db import models


class Activity(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default=uuid.uuid4, 
        editable = False
    )

    activity_name = models.CharField(max_length = 100, default = '')

    activity_average_rating = models.FloatField(default = 0.0)

    location = models.CharField(max_length = 100, default = '')

    starting_hour = models.CharField(max_length = 100, default = '')

    ending_hour = models.CharField(max_length = 100, default = '')

    description = models.CharField(max_length = 100, default = '')

    REQUIRED_FIELDS = []
    class Meta:
        app_label = "backend"