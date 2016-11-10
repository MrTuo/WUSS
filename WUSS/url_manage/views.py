
from __future__ import unicode_literals

from django.shortcuts import render
from models import Urls
import datetime
from django.http import HttpResponseRedirect



def add_url(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            url = request.POST.get('url', '')
            title= request.POST.get('title', '')
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
            update_fq =request.POST.get('update_fq', '1')
            track_status = request.POST.get('track_status', 'True')
            push_status = request.POST.get('push_status', 'True')
            user = request.user
            new_url = Urls(url=url, last_check_time=now, update_fq=update_fq,track_status=track_status, push_status= push_status,user=user,title=title)
            new_url.save()
            return HttpResponseRedirect('/')
        return render(request, 'add_url.html')

def delete_url(request, urlid):
    if request.user.is_authenticated():
        p = Urls.objects.get(id=urlid)
        p.delete()
        return HttpResponseRedirect('/')

def show_url(request):
    if request.user.is_authenticated():
        urls= Urls.objects.all()
        return render(request, "show_urls.html", {'urls':urls})


def edit_find(request,urlid):
    if request.user.is_authenticated():
    #urlid=request.POST.get('urlid', '')
        if request.method == 'POST' :
            urlid=request.POST.get('urlid', '')
            old = Urls.objects.get(id=urlid)
            new_url=request.POST.get('url', '')
            new_title=request.POST.get('title', '')
            new_update_fq = request.POST.get('update_fq', 0)
            new_track_status = request.POST.get('track_status', 'True')
            new_push_status = request.POST.get('push_statu', 'True')
            old.url=new_url
            old.title=new_title
            old.update_fq=new_update_fq
            old.track_status=new_track_status
            old.push_status=new_push_status
            old.save()
            return HttpResponseRedirect('/')
        print urlid
        edit_url=Urls.objects.get(id=urlid)
        return render(request, "edit_url.html", {'edit_url':edit_url})

