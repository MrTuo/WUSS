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
from Myuser import views;
<<<<<<< HEAD
from update_manage import views as updateviews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.logic),
    url(r'^homepage/$',views.logic),
    url(r'^judgelogic/$',views.judgelogic),
    url(r'^Register/$',views.Register),
    url(r'^gotoregiste/$',views.gotoregiste),
    url(r'^changeuser/$',views.changeuser),
    url(r'^gotochangeuser/$',views.gotochangeuser),
    url(r'^logout/$',views.logout),
    url(r'^error/$',views.error),
    url(r'^checkupdate/$',updateviews.check_update),
    url(r'^sendmail/$',updateviews.send_update_email),

=======
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.mainhomepage),
    url(r'^userhomepage/$',views.userhomepage),
    url(r'^usermanagement/$',views.usermanagement),
    url(r'^urlmanagement/$',views.urlmanagement),
    url(r'^logic/$',views.logic),
    url(r'^homepage/$',views.mainhomepage),
    url(r'^Register/$',views.Register),
    url(r'^changeuser/$',views.changeuser),
    url(r'^logout/$',views.logout),
    url(r'^error/$',views.error),
    url(r'^Userjudge/$',views.Userjudge),
    url(r'^text/$',views.text),
    url(r'^send_email/$',views.send_email),
    url(r'^forgetpassword/$',views.forgetpassword),
>>>>>>> 5a57dd37e3febc184b985be55e9d2de555d5dd86
]
