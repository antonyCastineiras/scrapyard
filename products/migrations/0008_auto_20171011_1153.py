# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_part_part_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='part_storage_locaion',
            new_name='part_storage_location',
        ),
    ]