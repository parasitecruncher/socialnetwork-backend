# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161103_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='highlighted',
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_image',
            field=models.ImageField(default='images/35b67fbe-090a-4909-bd62-634eae05a5e0', upload_to=b'', verbose_name='images/'),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='image',
            field=models.ImageField(default='images/fa40ce6c-6ef4-476f-a5a0-f329b9053865', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/c3f947a9-f4ec-4cf2-b533-85962a0173d4', upload_to='videos/'),
        ),
    ]
