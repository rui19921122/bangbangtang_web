# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_db', '0002_auto_20150822_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='attention_course',
            field=models.ManyToManyField(null=True, to='main_db.Course', verbose_name='关注课程'),
        ),
    ]
