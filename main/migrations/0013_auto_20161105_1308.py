# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 13:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20161105_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimages',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='uservideo',
            name='likes',
        ),
        migrations.AlterField(
            model_name='userimages',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserImages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/2db71302-3a54-406c-9599-02def66d7f9b', upload_to='videos/'),
        ),
    ]
