# coding=utf-8
from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals

from django.shortcuts import render
from url_manage.models import Urls
import datetime
from django.http import HttpResponseRedirect



def add_url(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        title= request.POST.get('title', '')
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        update_fq =request.POST.get('update_fq', '1')
        track_status = request.POST.get('track_status', 'True')
        push_status = request.POST.get('push_status', 'True')
        #user = request.user
        new_url = Urls(url=url, last_check_time=now, update_fq=update_fq,track_status=track_status, push_status= push_status,title=title)
        new_url.save()
        return HttpResponseRedirect('/')
    return render(request, 'add_url.html')

def delete_url(request, urlid):
    p = Urls.objects.get(id=urlid)
    p.delete()
    return HttpResponseRedirect('/')



