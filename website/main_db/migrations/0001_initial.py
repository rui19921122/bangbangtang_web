# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttentionCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('attention_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('category', models.CharField(verbose_name='类别', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='课程名称', max_length=50)),
                ('single_detail', models.CharField(verbose_name='课程简介', max_length=100, null=True)),
                ('start_time', models.DateField(verbose_name='开始时间')),
                ('text', models.CharField(verbose_name='课程介绍', max_length=200, null=True)),
                ('end_time', models.DateField(verbose_name='结束时间')),
                ('graphic_text_info', models.TextField(verbose_name='图文信息')),
                ('buy_time', models.DateTimeField(verbose_name='开放购买时间')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('price', models.IntegerField(verbose_name='价格', default=0)),
                ('sold', models.IntegerField(verbose_name='已售', default=0, null=True)),
                ('hot', models.BooleanField(verbose_name='是否为热门', default=False)),
                ('category', models.ForeignKey(verbose_name='类别', to='main_db.Category')),
            ],
            options={
                'ordering': ['-buy_time'],
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=8)),
                ('tel_phone', models.CharField(verbose_name='手机号码', max_length=11)),
                ('address', models.CharField(verbose_name='住址', max_length=100, null=True)),
                ('attention_course', models.ManyToManyField(verbose_name='关注课程', to='main_db.Course')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time', models.DateTimeField(verbose_name='评价时间')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('is_checked', models.NullBooleanField(verbose_name='是否已审核')),
                ('check_time', models.DateTimeField(verbose_name='审核时间', null=True)),
                ('commit_person', models.ForeignKey(verbose_name='评论人', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(verbose_name='课程', to='main_db.Course')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluateChange',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time', models.DateTimeField(verbose_name='成交时间')),
                ('add_or_des', models.BooleanField(verbose_name='增减')),
                ('num', models.IntegerField(verbose_name='增减数')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('num', models.IntegerField(editable=False, verbose_name='订单号')),
                ('order_time', models.DateTimeField(auto_now=True, verbose_name='下单时间')),
                ('end_time', models.DateTimeField(verbose_name='成交时间', null=True)),
                ('course', models.ForeignKey(verbose_name='课程', to='main_db.Course')),
                ('customer', models.ForeignKey(verbose_name='顾客', to='main_db.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='学校名称', max_length=15)),
                ('info', models.TextField(verbose_name='商家简介', null=True)),
                ('integral', models.IntegerField(verbose_name='积分', default=0, null=True)),
                ('tel_phone', models.IntegerField(verbose_name='手机号码')),
                ('place', models.CharField(verbose_name='地址', max_length=20, default='sa')),
            ],
        ),
        migrations.AddField(
            model_name='evaluatechange',
            name='order',
            field=models.ForeignKey(verbose_name='订单号', to='main_db.Order'),
        ),
        migrations.AddField(
            model_name='evaluatechange',
            name='school',
            field=models.ForeignKey(verbose_name='商家', to='main_db.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(to='main_db.School'),
        ),
        migrations.AddField(
            model_name='attentioncourse',
            name='course',
            field=models.ForeignKey(to='main_db.Course'),
        ),
        migrations.AddField(
            model_name='attentioncourse',
            name='customer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
