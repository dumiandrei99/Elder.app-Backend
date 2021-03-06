# Generated by Django 4.0.3 on 2022-06-19 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_post_post_description_alter_post_post_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=350)),
                ('post_uuid_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_uuid_comments', to='backend.post')),
                ('user_uuid_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_uuid_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
