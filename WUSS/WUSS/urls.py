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
from Myuser import views as myuserviews
from url_manage import views as manageviews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',views.mainhomepage),
    url(r'^$',myuserviews.userhomepage),
    url(r'^userhomepage/$',myuserviews.userhomepage),
    url(r'^usermanagement/$',myuserviews.usermanagement),
    url(r'^urlmanagement/$',myuserviews.urlmanagement),
    # url(r'^urlmanagement/$',manageviews.show_url),
    url(r'^login/$',myuserviews.login),
    url(r'^homepage/$',myuserviews.mainhomepage),
    url(r'^Register/$',myuserviews.Register),
    url(r'^changeuser/$',myuserviews.changeuser),
    url(r'^logout/$',myuserviews.logout),
    url(r'^error/$',myuserviews.error),
    url(r'^Userjudge/$',myuserviews.Userjudge),
    url(r'^text/$',myuserviews.text),
    url(r'^send_email/$',myuserviews.send_email),
    url(r'^forgetpassword/$',myuserviews.forgetpassword),
    #url(r'^checkupdate/$',updateviews.check_update),
    url(r'^Registerajax/$',myuserviews.Registerajax),
    url(r'^Registerajaxemail/$',myuserviews.Registerajaxemail),
    url(r'^send_email_to_changepassword/$',myuserviews.send_email_to_changepassword),
    url(r'^forgetandchangepassword/$',myuserviews.forgetandchangepassword),
    url(r'^applyfor/$',myuserviews.applyfor),
    url(r'^add_url/$', manageviews.add_url),
    url(r'^edit_find/(\d+)/$', manageviews.edit_find),
    url(r'^delete_url/(\d+)/$', manageviews.delete_url),
    url(r'^addhtmlurl/$',myuserviews.addhtmlurl),
    # url(r'^addhtmlurl/$',views.add_url_by_HTML),

    # url(r'^$', manageviews.show_url),
]
