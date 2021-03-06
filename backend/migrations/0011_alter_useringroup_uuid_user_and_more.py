# Generated by Django 4.0.3 on 2022-05-27 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_user_is_first_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useringroup',
            name='uuid_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uuid_user_group', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprefference',
            name='uuid_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uuid_user_prefference', to=settings.AUTH_USER_MODEL),
        ),
    ]
