# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_auto_20171118_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualification',
            name='Phd_year',
        ),
    ]