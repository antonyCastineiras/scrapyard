# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_part_listed_on_ebay'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='part_storage_locaion',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
