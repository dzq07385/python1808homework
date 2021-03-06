# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t03', '0004_auto_20180815_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u4eba\u540d')),
                ('age', models.IntegerField(verbose_name='\u5e74\u9f84')),
                ('height', models.FloatField(verbose_name='\u8eab\u9ad8')),
                ('salary', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u4eba\u540d')),
                ('age', models.IntegerField(verbose_name='\u5e74\u9f84')),
                ('height', models.FloatField(verbose_name='\u8eab\u9ad8')),
                ('face_score', models.IntegerField(verbose_name='\u989c\u503c')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
