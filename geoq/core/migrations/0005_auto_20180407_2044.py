# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-08 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180406_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aoi',
            name='status',
            field=models.CharField(default=b'Unassigned', max_length=15),
        ),
    ]