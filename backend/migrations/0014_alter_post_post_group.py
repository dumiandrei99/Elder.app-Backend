# Generated by Django 4.0.3 on 2022-06-18 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uuid_group', to='backend.group'),
        ),
    ]
