# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20170730_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='renthistory',
            name='sent_overdue_email',
            field=models.BooleanField(default=False, verbose_name='연체알람여부'),
        ),
    ]
