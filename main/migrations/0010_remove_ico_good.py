# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_ico_icoimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ico',
            name='good',
        ),
    ]
