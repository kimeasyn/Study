# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='study',
            name='start_date',
            field=models.DateField(),
        ),
    ]
