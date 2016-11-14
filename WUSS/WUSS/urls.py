# coding=utf-8
"""WUSS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Myuser import views
from update_manage import views as updateviews
from url_manage import views as manageviews


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',views.mainhomepage),
    url(r'^$',views.userhomepage),
    url(r'^userhomepage/$',views.userhomepage),
    url(r'^usermanagement/$',views.usermanagement),
    url(r'^urlmanagement/$',views.urlmanagement),
    # url(r'^urlmanagement/$',manageviews.show_url),
    url(r'^login/$',views.login),
    url(r'^homepage/$',views.mainhomepage),
    url(r'^Register/$',views.Register),
    url(r'^changeuser/$',views.changeuser),
    url(r'^logout/$',views.logout),
    url(r'^error/$',views.error),
    url(r'^Userjudge/$',views.Userjudge),
    url(r'^text/$',views.text),
    url(r'^send_email/$',views.send_email),
    url(r'^forgetpassword/$',views.forgetpassword),
    url(r'^checkupdate/$',updateviews.check_update),
    url(r'^Registerajax/$',views.Registerajax),
    url(r'^Registerajaxemail/$',views.Registerajaxemail),
    url(r'^send_email_to_changepassword/$',views.send_email_to_changepassword),
    url(r'^forgetandchangepassword/$',views.forgetandchangepassword),
    url(r'^applyfor/$',views.applyfor),
    url(r'^add_url/$', manageviews.add_url),
    url(r'^edit_find/(\d+)/$', manageviews.edit_find),
    url(r'^delete_url/(\d+)/$', manageviews.delete_url),
    # url(r'^$', manageviews.show_url),
    url(r'^sendmail/$',updateviews.show_update_info),
]
