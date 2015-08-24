from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=10,verbose_name='类别',null=False)
    def __str__(self):
        return self.category

class Course(models.Model):
    name = models.CharField(verbose_name='课程名称',null=False,max_length=50)
    school = models.ForeignKey('School')
    single_detail = models.CharField(verbose_name='课程简介',null=True,max_length=100) # todo find a better value
    category = models.ForeignKey(Category,verbose_name='类别',null=False)
    start_time = models.DateField(verbose_name='开始时间',null=False)
    text = models.CharField(verbose_name="课程介绍",null=True,max_length=200)
    end_time = models.DateField(verbose_name='结束时间',null=False)
    graphic_text_info = models.TextField(verbose_name='图文信息',null=False)
    buy_time = models.DateTimeField(verbose_name='开放购买时间',null=False)
    create_time = models.DateTimeField(verbose_name='创建时间',editable=False,auto_now=True)
    price = models.IntegerField(verbose_name='价格',null=False,default=0)
    sold = models.IntegerField(verbose_name='已售',null=True,default=0)
    hot = models.BooleanField(verbose_name='是否为热门',null=False,default=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-buy_time']
        verbose_name = '课程'

class Customer(models.Model):
    name = models.CharField(max_length=8,verbose_name='姓名',null=False)
    tel_phone = models.CharField(verbose_name='手机号码',null=False,max_length=11)
    address = models.CharField(verbose_name='住址',null=True,max_length=100)
    attention_course = models.ManyToManyField(Course,verbose_name='关注课程',null=True)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User)

class Evaluate(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',null=False)
    time = models.DateTimeField(verbose_name='评价时间',null=False)
    commit_person = models.ForeignKey(User,verbose_name='评论人',null=False)
    content = models.TextField(verbose_name='评论内容',null=False)
    is_checked = models.NullBooleanField(verbose_name='是否已审核',null=False)
    check_time = models.DateTimeField(verbose_name='审核时间',null=True)
    def __str__(self):
        return self.course + self.commit_person


class School(models.Model):
    name = models.CharField(max_length=15,verbose_name='学校名称',null=False)
    info = models.TextField(verbose_name='商家简介',null=True)
    integral = models.IntegerField(verbose_name='积分',null=True,default=0)
    tel_phone = models.CharField(verbose_name='手机号码',null=False,max_length=11)
    place = models.CharField(max_length=20,verbose_name='地址',null=False,default='sa')

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,verbose_name='顾客',null=False)
    num = models.IntegerField(verbose_name='订单号',editable=False)
    course = models.ForeignKey(Course,verbose_name='课程',null=False)
    order_time = models.DateTimeField(verbose_name='下单时间',null=False,editable=False,auto_now=True)
    end_time = models.DateTimeField(verbose_name='成交时间',null=True)

class EvaluateChange(models.Model):
    time = models.DateTimeField(verbose_name='成交时间',null=False)
    order = models.ForeignKey(Order,verbose_name='订单号',null=False)
    school = models.ForeignKey(School, verbose_name='商家', null=False)
    add_or_des = models.BooleanField(verbose_name='增减',null=False)
    num = models.IntegerField(verbose_name='增减数',null=False)

class AttentionCourse(models.Model):
    '关注课程'
    course = models.ForeignKey("Course")
    customer = models.ForeignKey(User)
    attention_time = models.DateTimeField(auto_now_add=True)
