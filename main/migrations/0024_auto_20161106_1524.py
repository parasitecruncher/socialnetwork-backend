# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20161106_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userimages',
            old_name='user',
            new_name='userr',
        ),
    ]
