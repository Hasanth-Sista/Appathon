# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=12)),
            ],
        ),
        migrations.DeleteModel(
            name='BusLocations',
        ),
    ]
