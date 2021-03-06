# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createmodels', '0003_auto_20161127_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='model',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='createmodels.Model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reference', to='createmodels.Model'),
        ),
    ]
