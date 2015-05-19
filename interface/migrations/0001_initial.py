# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('deleted', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('deleted', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=10, null=True)),
                ('address', models.TextField(null=True)),
                ('hours_of_operation', models.TextField(null=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('deleted', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='categories',
            field=models.ManyToManyField(related_name='items', to='interface.ServiceCategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='providers',
            field=models.ManyToManyField(related_name='items', to='interface.ServiceProvider'),
        ),
    ]
