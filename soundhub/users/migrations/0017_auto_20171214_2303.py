# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to=users.models.profile_image_directory_path),
        ),
    ]
