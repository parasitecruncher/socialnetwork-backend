# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20161103_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_image',
            field=models.ImageField(upload_to=b'', verbose_name='images/'),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='image',
            field=models.ImageField(default='images/d867d563-a8aa-4af9-93ed-750ab9120ba6', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/0793ade7-9f8d-4314-b1e9-bdc178c50c44', upload_to='videos/'),
        ),
    ]
