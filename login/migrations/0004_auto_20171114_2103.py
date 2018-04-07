# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Designation',
            new_name='Academic_position',
        ),
        migrations.AddField(
            model_name='profile',
            name='About',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='Faculty_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
