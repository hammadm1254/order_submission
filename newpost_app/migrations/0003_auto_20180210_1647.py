# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newpost_app', '0002_auto_20180210_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='special_insturctions',
            new_name='special_instructions',
        ),
    ]
