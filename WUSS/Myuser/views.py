from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
import MySQLdb

def homepage(request):
    db = MySQLdb.connect(user='root', db='WUSS_User', passwd='501874997', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Myuser_myuser')
    names = [row[1] for row in cursor.fetchall()]
    db.close()
    print names
    if names[0]=='501874997@qq.com':
        return render(request, 'homepage.html')
    else:
        return render(request, 'error.html')

def Register(request):
    return render(request, 'Register.html')

def text(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    if request.method == 'POST':
        username = request.POST.get('Myuser.name','')
        password = request.POST.get('Myuser.password','')
        user = auth.authenticate(username=username,password=password);

    return render(request, 'text.html')
