# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171207_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_anonymous',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
