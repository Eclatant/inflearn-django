# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0002_guessnumbers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guessnumbers',
            name='lottos',
            field=models.CharField(max_length=120),
        ),
    ]
