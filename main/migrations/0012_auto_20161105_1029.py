# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20161105_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uservideo',
            old_name='likkes',
            new_name='likes',
        ),
        migrations.AlterField(
            model_name='userimages',
            name='image',
            field=models.ImageField(default='images/b01f533b-3992-4796-abd2-11752cc01c9d', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/f2b76f92-11b2-4c6c-9440-7039b7ffba10', upload_to='videos/'),
        ),
    ]
