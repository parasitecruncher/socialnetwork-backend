# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20161105_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/dad295f8-fd27-4d91-805f-88678de7d24a', upload_to='videos/'),
        ),
    ]
