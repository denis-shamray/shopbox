# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_msg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='url',
        ),
        migrations.AlterField(
            model_name='msg',
            name='usermsg',
            field=models.TextField(),
        ),
    ]