# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0003_auto_20171024_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
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
        migrations.AlterField(
            model_name='study',
            name='title',
            field=models.CharField(help_text='제목을 입력하세요', max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='study',
            name='writer',
            field=models.CharField(max_length=100, verbose_name='글쓴이'),
        ),
    ]
