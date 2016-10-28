from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Myuser import models
from django.core.mail import send_mail
from smtplib import SMTPException
from django.conf import settings

import time
def userhomepage(request):#进入用户页面主页
    content = {
        'user_is_logic': 'YES',
        'user': request.user,
        'chooise':1,
    }
    return render(request, 'userhomepage.html', content)

def usermanagement(request):#进入用户账号管理页面
    if request.user.is_authenticated():
        content={
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':2,
            'chooise_user_left_nav':1,
            'username':request.user,
            'useremail':request.user.email,
            'usertime':request.user.last_login,
        }
        return render(request,'UserManageCenter.html',content)
    return HttpResponseRedirect('/error')

def urlmanagement(request):
    if request.user.is_authenticated():
        content={
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':3,
            'chooise_user_left_nav':1,
        }
        return render(request,'URLmanagement.html',content)
    return HttpResponseRedirect('/error')
def Userjudge(request):#判断是否登录
    print(request.user)
    if request.user.is_authenticated():
        return HttpResponseRedirect("/userhomepage")
    else:
        return HttpResponseRedirect("/logic")

def mainhomepage(request):#进入到主页
    if request.user.is_authenticated():
        content={
            'user_is_logic':'YES'
        }
        return render(request,'homepage1.html',content)
    content={
        'user':'登录'
    }
    return render(request,'homepage1.html',content)

def logic(request):#登录
    print(request.user)
    if request.user.is_authenticated():
        content = {
            'user_is_logic': 'YES',
            'user':request.user,
        }
        return render(request, 'userhomepage.html',content)
    if request.method == 'POST':
        logname = request.POST.get('username', '')
        logpassword = request.POST.get('password', '')
        user = auth.authenticate(username=logname, password=logpassword)
        if user is not None:
            print("0000000")
            auth.login(request, user)
            # return render(request,'homepage.html')
            content={
                'user_is_logic':'YES',
                'user':logname,
            }
            return render(request, 'homepage1.html', content)
        return HttpResponseRedirect("/error")
    return render(request, 'logic.html')

def Register(request):#注册
    # if request.user.is_authenticated():  #如果登录了就不用在注册了
    #     return HttpResponseRedirect("/user")
    if request.method == 'POST':
        registname = request.POST.get('idname', '')
        registemail = request.POST.get('idemail', '')
        registpassword = request.POST.get('idpassword', '')
        filterResult = User.objects.filter(username=registname)  # 判断用户是否存在
        filterResultemail = User.objects.filter(email=registemail) #判断email是否存在
        if len(filterResult) > 0 or len(filterResultemail) > 0:
            return render(request, 'error.html')  # 如果存在在这里先跳转到错误页面
        user = User()  # 将用户的资料存入到数据库中
        user.username = registname
        user.set_password(registpassword)
        user.email = registemail
        user.save()
        return HttpResponseRedirect('/logic')
    return render(request, 'Register.html')

def error(request):#错误页面
    return render(request,'error.html')

def changeuser(request):#修改密码
    if request.user.is_authenticated():
        user = request.user
        content={
            'username':user.username,
            'chooise_user_left_nav':2,
        }
    if request.method == "POST":
        username = user.username
        oldpassword = request.POST.get('oldpassword', '')
        newpassword = request.POST.get('newpassword', '')
        user = auth.authenticate(username=username, password=oldpassword)
        if user is not None and user.is_active:
            user.set_password(newpassword)
            user.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect('/error')
    return render(request,'changeuser.html',content)


@login_required
def logout(request):#登出
    auth.logout(request)
    return HttpResponseRedirect("/")  # 返回到登录界面


def text(request):

    return render(request,'text.html')


def send_email(request):
    subject = u'号码通激活'
    name = "帅哥"
    print(name)
    message = u'用户:' + name + u' 您好，首先非常感谢你的注册' \
              + u"\n点击链接就可以激活邮箱，从而用邮箱进行登陆:" \
              + u"http://192.168.1.163:8080/account/activate/?activation_key="  \
              + u"\n我们将为你提供非常好的号码相关服务：比如号码备份/群组建立/号码查找/群组活动等等,来自108网络教研室"

    print(message)
    send_mail(subject, message, settings.EMAIL_HOST_USER, ['501874997@qq.com'])
    return HttpResponseRedirect("/")