from __future__ import unicode_literals

from django.shortcuts import render
from Myuser.models import *
from url_manage.models import *
from update_manage.models import *
import datetime
import re
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from url_manage.models import Urls
from update_manage.models import *
import urllib.request
from update_manage.views import get_cache_file
@login_required(login_url='/login/')
def add_url(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            url = request.POST.get('url', '')
            title = request.POST.get('title', '')
            time = request.POST.get('time', '')
            time = re.split(r':|：',time)
            # yesterday = datetime.datetime.now() - datetime.timedelta(days=1) # 获取昨天的时间
            # last_check_time = datetime.datetime(yesterday.year,yesterday.month,yesterday.day,int(time[0]),int(time[1]))
            now = datetime.datetime.now()  # 获取斤天的时间
            last_check_time = datetime.datetime(now.year, now.month, now.day, int(time[0]),
                                                int(time[1]))
            update_fq = request.POST.get('update_fq', '1')
            track_status = request.POST.get('track_status', 'True')
            user = request.user
            type = request.POST.get('type', '')  # 区分普通url和rssurl
            spider_guide = request.POST.get('spider_guide', '')  # 若为空代表为RSSurl，不空则为普通URL
            new_url = Urls(url=url,
                           last_check_time=last_check_time,
                           update_fq=update_fq,
                           track_status=track_status,
                           user=user,
                           title=title,
                           type=type,
                           spider_guide=spider_guide,
                           )
            new_url.save()
            if type == '1':  # 保存一般url的items
                item_strs = spider_guide.split(';')
                item_strs.remove('')# 删除空元素
                for item_str in item_strs:
                    new_item = SpiderItem(
                        attr_str = item_str,
                        url=new_url
                    )
                    new_item.save()
            cacheurl = CacheFile.objects.filter(url=url)# 查找是否已经保存url
            if not cacheurl : # 未保存
                new_cachefile = CacheFile(url=url)
                new_cachefile.save()
            return HttpResponseRedirect('/urlmanagement/')
        content = {
            'user_is_logic': 'YES',
            'chooise_user_left_nav':2,
        }
        return render(request, 'add_url.html', content)

@login_required(login_url='/login/')
def delete_url(request, urlid):
    if request.user.is_authenticated():
        p = Urls.objects.get(id=urlid)
        old_url=p.url
        if p.type==True:
            SpiderItem.objects.filter(url=p).delete()
        else :
            RssItem.objects.filter(url=p).delete()
        p.delete()
        # 删除已经失效的cachefile
        if not Urls.objects.filter(url=old_url, track_status=1):
            CacheFile.objects.filter(url=old_url).delete()


        return HttpResponseRedirect('/urlmanagement/')

@login_required(login_url='/login/')
def show_url(request):
    if request.user.is_authenticated():
        urls = Urls.objects.get(user=request.user)
        # urls= Urls.objects.all()
        return render(request, "show_urls.html", {'urls': urls})

@login_required(login_url='/login/')
def edit_find(request, urlid):
    if request.user.is_authenticated():
        # urlid=request.POST.get('urlid', '')
        if request.method == 'POST':
            old = Urls.objects.get(id=urlid)
            old_url = old.url
            new_url = request.POST.get('url', '')
            new_title = request.POST.get('title', '')
            new_update_fq = request.POST.get('update_fq', 1)

            time = request.POST.get('time', '')
            time = re.split(r':|：', time)
            # yesterday = datetime.datetime.now() - datetime.timedelta(days=1)  # 获取昨天的时间
            # last_check_time = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, int(time[0]), int(time[1]))

            now = datetime.datetime.now()  # 获取斤天的时间
            last_check_time = datetime.datetime(now.year, now.month, now.day, int(time[0]),
                                                int(time[1]))
            new_track_status = request.POST.get('track_status', 'True')
            spider_guide = request.POST.get('spider_guide', '')  # 若为空代表为RSSurl，不空则为普通URL
            old.url = new_url
            old.title = new_title
            old.update_fq = new_update_fq
            old.track_status = new_track_status
            old.spider_guide = spider_guide
            old.last_check_time = last_check_time
            old.save()
            # 保存item
            if old.type == True:
                SpiderItem.objects.filter(url=old).delete()
                item_strs = spider_guide.split(';')
                item_strs.remove('')  # 删除空元素
                for item_str in item_strs:
                    new_item = SpiderItem(
                        attr_str=item_str,
                        url=old
                    )
                    new_item.save()

            # 删除已经失效的cachefile
            if not Urls.objects.filter(url=old_url, track_status=1):
                CacheFile.objects.filter(url=old_url).delete()

            cacheurl = CacheFile.objects.filter(url=new_url)  # 查找是否已经保存url
            if not cacheurl:  # 未保存
                new_cachefile = CacheFile(url=new_url)
                new_cachefile.save()
            return HttpResponseRedirect('/')
        edit_url = Urls.objects.get(id=urlid)

        if edit_url.type == False:
            content = {
                'user_is_logic': 'YES',
                'edit_url': edit_url,
                'chooise_user_left_nav':2,
            }
            return render(request, "edit_url.html", content)
        else:
            html = get_cache_file(edit_url.url)  # 从缓存中加载html

            if not html:  # 若缓存中没有，则使用爬虫爬取
                rq = urllib.request.Request(edit_url.url)
                rq.add_header("user-agent", "Mozilla/5.0")  # 伪装浏览器
                response = urllib.request.urlopen(rq)
                html = response.read()
                try:
                    html = html.decode('UTF-8')
                except:
                    try:
                        html = html.decode('gb2312')
                    except:
                        try:
                            html = html.decode('ANSI')
                        except:
                            try:
                                html = html.decode('GBK')
                            except:
                                try:
                                    html = html.decode('UNICODE')
                                except:
                                    html = html.decode('ASCII')
            content = {
                'user_is_logic': 'YES',
                'edit_url': edit_url,
                'htmlurl':html,
            }
            return render(request, "edit2_url.html", content)

@login_required(login_url='/login/')
def addhtmlurl(request):
    url=request.GET.get('url1')
    html = get_cache_file(url) # 从缓存中加载html
    print(url)
    if not html : # 若缓存中没有，则使用爬虫爬取
        rq = urllib.request.Request(url)
        rq.add_header("user-agent", "Mozilla/5.0")  # 伪装浏览器
        response = urllib.request.urlopen(rq)
        html = response.read()
        try:
            html=html.decode('UTF-8')
        except:
            try:
                html=html.decode('gb2312')
            except:
                try:
                    html = html.decode('ANSI')
                except:
                    try:
                        html = html.decode('GBK')
                    except:
                        try:
                            html = html.decode('UNICODE')
                        except:
                            html = html.decode('ASCII')

    content={
        'htmlurl':html,
        'url':url,
    }
    return render(request, 'addhtmlurl.html', content)
