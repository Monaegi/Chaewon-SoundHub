# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct_messages', '0004_message_is_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
        migrations.AddField(
            model_name='message',
            name='read_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
