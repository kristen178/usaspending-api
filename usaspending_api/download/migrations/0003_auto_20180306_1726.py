# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-06 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_auto_20180216_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadjob',
            name='file_size',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
