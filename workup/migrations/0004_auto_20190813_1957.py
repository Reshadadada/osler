# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-14 00:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workup', '0003_historicalworkup_add_attending_validator_20190324_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workup',
            name='clinic_day',
            field=models.ForeignKey(help_text=b'When was the patient seen?', on_delete=django.db.models.deletion.CASCADE, to='workup.ClinicDate'),
        ),
    ]
