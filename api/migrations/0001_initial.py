# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cars',
                'verbose_name': 'Car',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'CarModels',
                'verbose_name': 'CarModel',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Manufacturers',
                'verbose_name': 'Manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('replaced_parts', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Car')),
            ],
            options={
                'verbose_name_plural': 'Services',
                'verbose_name': 'Service',
            },
        ),
        migrations.AddField(
            model_name='carmodel',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Manufacturer'),
        ),
    ]
