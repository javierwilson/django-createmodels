# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createmodels', '0010_auto_20161127_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='verbose',
            new_name='verbose_name',
        ),
    ]