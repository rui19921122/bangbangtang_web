__author__ = 'Administrator'
from django import forms
from django.forms.util import ErrorList
from django.forms import TextInput, PasswordInput
from django.forms.util import ValidationError
from main_db.models import Customer
from django.db.models import Q


class RegisterTextInput(TextInput):
    def __init__(self, text, ):
        super(RegisterTextInput, self).__init__()
        self.attrs = {'class': 'input-weak', 'placeholder': text, 'type': 'password'}


class RegisterPasswordInput(PasswordInput):
    def __init__(self, text, ):
        super(RegisterPasswordInput, self).__init__()
        self.attrs = {'class': 'input-weak', 'placeholder': text, 'type': 'password'}



class RegisterForm(forms.Form):
    name = forms.CharField(max_length=15, label='用户名', widget=forms.TextInput(attrs={'class': 'input-weak',
                                                                                     'placeholder': '用户名'}))
    tel = forms.CharField(label="电话", widget=RegisterTextInput("电话", ))
    place = forms.CharField(label='住址',widget=RegisterTextInput("住址",))
    email = forms.EmailField(label='电子邮箱',widget=RegisterTextInput("电子邮箱",))
    password = forms.CharField(widget=RegisterPasswordInput('请输入密码'))
    password_conf = forms.CharField(widget=RegisterPasswordInput("再次输入密码"))

    def clean_name(self):
        name = self.cleaned_data['name']
        if Customer.objects.filter(name=name):
            raise ValidationError("用户名已被使用")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email):
            raise ValidationError("电子邮箱已被注册")
        return email

    def clean_tel(self):
        tel = self.cleaned_data['tel']
        if len(tel) == 11 and tel.startswith(('13','15','17')):
            if Customer.objects.filter(tel_phone=tel):
                raise ValidationError("手机号已经被使用")
            return tel
        else:
            raise ValidationError("请输入正确的手机号")


    def clean(self):
        super(RegisterForm,self).clean()
        if self.errors:
            return
        name = self.cleaned_data['name']
        tel = self.cleaned_data['tel']
        password = self.cleaned_data['password']
        password_conf = self.cleaned_data['password_conf']
        if password != password_conf:
            self.add_error('password','两次输入的密码不一致')
            return
        if len(password) < 6:
            self.add_error('password','您的密码过短')
        return
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,widget=RegisterTextInput("输入您的用户名/手机号/电子邮箱"))
    pwd = forms.CharField(widget=RegisterPasswordInput("请输入您的密码"))

