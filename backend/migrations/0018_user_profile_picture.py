# Generated by Django 4.0.3 on 2022-06-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_remove_post_post_likes_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]