# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-30 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(max_length=40),
        ),
    ]
