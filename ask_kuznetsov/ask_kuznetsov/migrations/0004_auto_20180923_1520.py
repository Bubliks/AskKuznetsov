# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-23 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_kuznetsov', '0003_auto_20180918_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
