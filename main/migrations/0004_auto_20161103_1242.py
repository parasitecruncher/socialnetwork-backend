# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161103_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_image',
            field=models.ImageField(default='images/eeb5f631-bbc5-4749-a5f5-374f93af74a1', upload_to=b'', verbose_name='images/'),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='image',
            field=models.ImageField(default='images/2fc71892-16bf-4866-b6e1-00db93322bb0', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/413801da-2ef8-4d15-84a8-b8dee7322187', upload_to='videos/'),
        ),
    ]
