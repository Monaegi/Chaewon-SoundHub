# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20171129_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('S', 'Soundhub'), ('G', 'Google'), ('F', 'Facebook'), ('N', 'Naver')], default='S', max_length=1),
        ),
    ]