# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u8bed\u8a00\u540d\u5b57')),
            ],
        ),
    ]
