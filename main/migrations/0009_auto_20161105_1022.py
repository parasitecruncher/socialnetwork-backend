# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20161103_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstatus',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userimages',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='userimages',
            name='user',
        ),
        migrations.AddField(
            model_name='userimages',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likers', to='main.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='image',
            field=models.ImageField(default='images/be809a5d-aa09-46e0-890c-fc5ef8163108', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uservideo',
            name='image',
            field=models.FileField(default='videos/71bc92b6-d705-49e4-b2df-603e5298ac37', upload_to='videos/'),
        ),
        migrations.DeleteModel(
            name='UserStatus',
        ),
    ]
