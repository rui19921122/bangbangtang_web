from django.shortcuts import render
from django.http import request, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from main_db.models import Course, Customer, AttentionCourse, School, Evaluate
from main_db.form import RegisterForm, LoginForm


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        attention = AttentionCourse.objects.filter(customer=user)[:5]
        attention_course = []
        attention_course_id = []
        for i in attention:
            attention_course.append(i.course)
            attention_course_id.append(i.id)
        f = Course.objects.all()[:9]
        new = []
        for i in f:
            if i.id in attention_course_id:
                pass
            else:
                new.append(i)
        return render(request, 'mobile/index.html', {'courses': new, 'attention_course': attention_course})
    else:
        f = Course.objects.all()[:9]
        return render(request, 'mobile/index.html', {'courses': f, })


def search(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request, 'mobile/search.html')


def login_in(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponseRedirect('/account')
    else:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['username']
                pwd = login_form.cleaned_data['pwd']
                try:
                    usr = Customer.objects.get(Q(name=name) | Q(tel_phone=name) | Q(email=name)).user.username
                except:
                    login_form.add_error('username', "没有此用户")
                    return render(request, 'mobile/login.html', {'form': login_form})
                check = authenticate(username=usr,password=pwd)
                if check:
                    login(request,check)
                    return HttpResponseRedirect('/account')
                else:
                    login_form.add_error('pwd', '错误的密码')
                    return render(request, 'mobile/login.html', {'form': login_form})
            else:
                return render(request, 'mobile/login.html', {'form': login_form})
        elif request.method == 'GET':
            login_form = LoginForm()
            return render(request, 'mobile/login.html', {'form': login_form})


def register(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/my')
    if request.method == "POST":
        form = RegisterForm(request.POST, )
        if form.is_valid():
            data = form.cleaned_data
            new = User.objects.create_user(username=data['name'], email='1@qq.com', password=data['password'])
            new_detail = Customer(name=data['name'], tel_phone=data['tel'], user=new, address='默认地址')
            print(new)
            print(new_detail)
            new.save()
            new_detail.save()
            user = authenticate(username=data['name'], password=data['password'])
            login(request, user)
            return HttpResponseRedirect('/detail')
        else:
            return render(request, 'mobile/register.html', {'form': form})
    elif request.method == "GET":
        form = RegisterForm()
        return render(request, 'mobile/register.html', {"form": form})


def order(request):
    return render(request, 'mobile/order.html')

@login_required(login_url='login_in')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def account(request):
    user = Customer.objects.get(user=request.user)
    attention_ = AttentionCourse.objects.filter(customer=request.user)
    attention = []
    for i in attention_:
        attention.append(i.course)
    return render(request, 'mobile/account.html', {'user': user, 'attention': attention})


def course(request, course_id):
    course_obj = Course.objects.filter(id=course_id)
    comment = Evaluate.objects.filter(course=course_obj, is_checked=True)[:4]
    comment_count = Evaluate.objects.filter(course=course_obj, is_checked=True).count()
    if comment.count() == 4:
        more_comment = True
    else:
        more_comment = False
    if course_obj.count() == 1:
        return render(request, 'mobile/course.html', {'course': course_obj[0], 'comment': comment[:3],
                                                      'more_comment': more_comment,
                                                      'comment_count': comment_count})
    else:
        raise Http404


def comment_list(request, course_id):
    course_obj = Course.objects.filter(id=course_id)
    comment = Evaluate.objects.filter(course=course_obj, is_checked=True)
    return render(request, 'mobile/comment_list.html', {'comment': comment})
