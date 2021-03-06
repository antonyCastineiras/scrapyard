# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20171011_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Part')),
            ],
        ),
    ]
