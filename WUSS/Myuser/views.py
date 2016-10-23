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
    return render(request, 'logic.html')

def Register(request):
    return render(request, 'Register.html')

def judgelogic(request):
    logname = request.POST.get('username', '')
    logpassword = request.POST.get('password', '')
    user = auth.authenticate(username=logname, password=logpassword)
    if  user is not None:
        auth.login(request, user)
        return render(request,'homepage.html')
    return render(request,'logic.html')

def gotoregiste(request):
    registname=request.POST.get('idname','')
    registemail=request.POST.get('idemail','')
    registpassword=request.POST.get('idpassword','')
    filterResult = User.objects.filter(username=registname)  # c************
    if len(filterResult) > 0:
        return render(request,'error.html')
    user = User()  # d************************
    user.username = registname
    user.set_password(registpassword)
    user.email = registemail
    user.save()
    return render(request,'logic.html')
