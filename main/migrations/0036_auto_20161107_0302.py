# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20161107_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_image',
            field=models.ImageField(blank=True, default='/media/anonymous.png', upload_to=b''),
        ),
    ]