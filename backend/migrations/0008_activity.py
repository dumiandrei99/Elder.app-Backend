# Generated by Django 4.0.3 on 2022-05-14 20:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_useringroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=100)),
            ],
        ),
    ]
