# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170930_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='listed_on_ebay',
            field=models.BooleanField(default=False),
        ),
    ]
