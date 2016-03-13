# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=200)),
                ('tag_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LocationPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=50)),
                ('location_long', models.IntegerField(default=0)),
                ('location_lat', models.IntegerField(default=0)),
                ('migration_stage', models.CharField(max_length=50)),
                ('migration_status', models.CharField(max_length=50)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='migration_csv_import',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('timestamp', models.CharField(max_length=50)),
                ('location_long', models.FloatField()),
                ('location_lat', models.FloatField()),
                ('individual_local_identifier', models.IntegerField()),
                ('study_name', models.CharField(max_length=200)),
            ],
        ),
    ]
