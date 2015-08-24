# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='tel_phone',
            field=models.CharField(max_length=11, verbose_name='手机号码'),
        ),
    ]
