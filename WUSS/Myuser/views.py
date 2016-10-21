from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import MySQLdb
from Myuser import models
import time

def logic(request):
    return render(request, 'logic.html')

def Register(request):
    return render(request, 'Register.html')

def judgelogic(request):
    logname = request.POST.get('username', '')
    logpassword = request.POST.get('password', '')
    db = MySQLdb.connect("localhost","root","501874997","wuss" )
    cursor = db.cursor()
    sql="SELECT password FROM auth_user where username='%s'" % (logname)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    if results[0][0]==logpassword:
        return render(request,'homepage.html')
    else:
        return render(request,'error.html')

def gotoregiste(request):
    registname=request.POST.get('idname','')
    registemail=request.POST.get('idemail','')
    registpassword=request.POST.get('idpassword','')
    last_login=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    date_joined=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print registname
    # db = MySQLdb.connect("localhost","root","501874997","wuss")
    # cursor = db.cursor()
    # sql = "insert into auth_user values(null,'%s','%s',0,'%s','null','null','%s',0,0,'%s')" %(registpassword,last_login,registname,registemail,date_joined)
    # cursor.execute(sql)
    # db.commit()
    # db.close()
    return render(request,'logic.html')
