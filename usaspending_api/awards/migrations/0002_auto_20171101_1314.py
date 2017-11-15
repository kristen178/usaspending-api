# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionfabs',
            name='awarding_office_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfabs',
            name='funding_office_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfabs',
            name='legal_entity_city_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfabs',
            name='legal_entity_country_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfabs',
            name='place_of_perform_country_n',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfabs',
            name='place_of_perform_county_c',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfpds',
            name='award_or_idv_flag',
            field=models.TextField(blank=True, null=True),
        ),
    ]