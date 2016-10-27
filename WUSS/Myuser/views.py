# coding=utf-8
from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Myuser import models

import time

def logic(request):
    if request.user.is_authenticated():
        return render(request, 'homepage.html')
    return render(request, 'logic.html')

def Register(request):
    return render(request, 'Register.html')

def error(request):
    return render(request,'error.html')

def judgelogic(request):
    logname = request.POST.get('username', '')
    logpassword = request.POST.get('password', '')
    user = auth.authenticate(username=logname, password=logpassword)
    if  user is not None:
        auth.login(request, user)
        # return render(request,'homepage.html')
        try:
            return HttpResponseRedirect(request.GET['next'])
        except:
            return HttpResponseRedirect('/homepage')
    return HttpResponseRedirect("/")

def gotoregiste(request):
    # if request.user.is_authenticated():  #如果登录了就不用在注册了
    #     return HttpResponseRedirect("/user")
    registname=request.POST.get('idname','')
    registemail=request.POST.get('idemail','')
    registpassword=request.POST.get('idpassword','')
    filterResult = User.objects.filter(username=registname)  #判断用户是否存在
    if len(filterResult) > 0:
        return render(request,'error.html')#如果存在在这里先跳转到错误页面
    user = User()  # 将用户的资料存入到数据库中
    user.username = registname
    user.set_password(registpassword)
    user.email = registemail
    user.save()
    return render(request,'logic.html')#返回到登录界面

def changeuser(request):
    if request.user.is_authenticated():
        user = request.user
        content={
            'username':user.username
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
        print("yess")
    return render(request,'changeuser.html',content)

def gotochangeuser(request):
    user = request.user




    return HttpResponseRedirect("error")
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")  # 返回到登录界面