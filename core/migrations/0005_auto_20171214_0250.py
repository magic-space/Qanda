# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 02:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171211_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='downvotes',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]