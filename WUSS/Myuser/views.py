# This Python file uses the following encoding: utf-8

from django.shortcuts import render,render_to_response,HttpResponse,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from Myuser import models
from django.core.mail import send_mail
from django.conf import settings
from random import Random
import time
from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist
from Myuser.models import VerificationCode



#encoding:utf-8
def userhomepage(request):#into the userhomepage
    if request.user.is_authenticated():
        content = {
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':1,
            'chooise_user_left_nav':1,
        }
        return render(request, 'userhomepage.html', content)
    return HttpResponseRedirect('/error')

def usermanagement(request):#into the UserManageCenter
    if request.user.is_authenticated():
        content={
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':2,
            'chooise_user_left_nav':1,
            'username':request.user,
            'useremail':request.user.email,
            'usertime':request.user.last_login,
        }
        return render(request,'UserManageCenter.html',content)
    return HttpResponseRedirect('/error')

def urlmanagement(request):#URL management
    if request.user.is_authenticated():
        content={
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':3,
            'chooise_user_left_nav':1,
        }
        return render(request,'URLmanagement.html',content)
    return HttpResponseRedirect('/error')


def Userjudge(request):# if login or not
    if request.user.is_authenticated():
        return HttpResponseRedirect("/userhomepage")
    else:
        return HttpResponseRedirect("/login")
#encoding:utf-8
def mainhomepage(request):#into the homepage
    if request.user.is_authenticated():
        content={
            'user_is_logic':'YES'
        }
        return render(request,'homepage1.html',content)
    content={
        'user':'登录'
    }
    return render(request,'homepage1.html',content)

def login(request):#login
    if request.user.is_authenticated():
        content = {
            'user_is_logic': 'YES',
            'user':request.user,
        }
        return render(request, 'userhomepage.html',content)
    if request.method == 'POST':
        # logname = request.POST.get('username', '')
        # if logname=='':
        lognameforajax =request.POST['lognameforajax'].strip()
        # logpassword = request.POST.get('password', '')
        # if logpassword=='':
        logpasswordforajax = request.POST['logpasswordforajax'].strip()
        user = auth.authenticate(username=lognameforajax,password=logpasswordforajax)
        #user = auth.authenticate(username=logname)
        if user is not None:#表示用户找到了
            auth.login(request, user)
            content={
                'user_is_logic':'YES',
                'user':lognameforajax,
            }
            print(user)
            return render(request,'homepage1.html', content)
        else:
            return HttpResponse("账号或密码错误")

    return render(request, 'login.html')

def Register(request):#register
    if request.method == 'POST':
        registname = request.POST.get('idname', '')
        registemail = request.POST.get('idemail', '')
        registpassword = request.POST.get('idpassword', '')

        filterResult = User.objects.filter(username=registname)  # judge the exciting of user
        filterResultemail = User.objects.filter(email=registemail) #judge the exciting of email
        if len(filterResult) > 0 or len(filterResultemail) > 0:
            return render(request, 'error.html')  # if yes ,go to the error
        user = User()  # save the user
        user.username = registname
        user.set_password(registpassword)
        user.email = registemail
        user.save()
        return HttpResponseRedirect('/logic')
    return render(request, 'Register.html')

def Registerajax(request):#judge if the username exciting or not
    name=request.POST['name'].strip()
    try:
        user=User.objects.get(username=name)
    except:
        return HttpResponse("可以使用该用户名")
    return HttpResponse("用户已存在")


def Registerajaxemail(request):#judge if the email exciting or not
    email = request.POST['email'].strip()
    try:
        user = User.objects.get(email=email)
    except:
        return HttpResponse("可以使用该邮箱")
    return HttpResponse("邮箱已注册")

def error(request):#error
    return render(request,'error.html')

def changeuser(request):#change password  PS:remeber the username and oldpassword
    if request.user.is_authenticated():
        user = request.user
        content={
            'username':user.username,
            'chooise_user_left_nav':2,
            'user_is_logic': 'YES',
            'chooise':2,
        }
    if request.method == 'POST' and request.user.is_authenticated():
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
    return render(request,'changeuser.html',content)


@login_required
def logout(request):#exiting
    auth.logout(request)
    return HttpResponseRedirect("/")  # return to the login



# def send_email(request):
#     yanzhengma=random_str()
#     subject = u'号码通激活'
#     mail_list=['501874997@qq.com',]
#     from_email=settings.EMAIL_HOST_USER
#     name = "帅哥"
#     print(name)
#     message = u'用户:' + name + u' 您好，首先非常感谢你的注册' +yanzhengma\
#               + u"\n点击链接就可以激活邮箱，从而用邮箱进行登陆:" \
#               + u"http://192.168.1.163:8080/account/activate/?activation_key="  \
#               + u"\n我们将为你提供非常好的号码相关服务：比如号码备份/群组建立/号码查找/群组活动等等,来自108网络教研室"
#     send_mail(subject, message, settings.EMAIL_HOST_USER, [])
#     email_template_name = 'text.html'
#     t = loader.get_template(email_template_name)
#     html_content = t.render()
#     msg = EmailMultiAlternatives(subject, html_content, from_email, mail_list)
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#     return HttpResponseRedirect("/")
def send_email(request):
    subject = u'测试'
    name = "帅哥"
    mail_list = ['501874997@qq.com' ,]#recipients
    from_email = settings.EMAIL_HOST_USER#addressor
    message = u'用户:' + name + u' 这是测试邮件'
    email_template_name = 'send_email_template.html'#email html
    t = loader.get_template(email_template_name)
    html_content = t.render()
    msg = EmailMultiAlternatives(subject, html_content, from_email, mail_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # send_mail(subject, message, from_email, mail_list)
    return HttpResponseRedirect("/")

def send_email_to_changepassword(request):
    yanzhengma = random_str()
    email=request.POST['email'].strip()
    print(email)
    try:
        user=User.objects.get(email=email)
    except:
        print("herer")
        return HttpResponse("邮箱未注册无法发送")
    try:
        VCodeUser = VerificationCode.objects.get(email=email)
        VCodeUser.VCode = yanzhengma
        VCodeUser.save()
    except:
        VCodeUser = VerificationCode()
        VCodeUser.email = email
        VCodeUser.VCode = yanzhengma
        VCodeUser.save()
    subject = u'WUSS用户忘记密码'
    from_email=settings.EMAIL_HOST_USER
    message = u'亲爱的用户:'+ email + "您在WUSS请求的验证码是:"+yanzhengma
    send_mail(subject, message, from_email, [email,])
    return HttpResponse("发送成功")


def forgetpassword(request):#forget password
    return render(request,'forget_password.html')

def applyfor(request):
    email = request.POST['email'].strip()
    yanzhengma1=request.POST['yanzhengma'].strip()
    try:
        VCodeUser=VerificationCode.objects.get(email=email)
        VCode=VCodeUser.VCode
    except:
        return HttpResponse("两次邮箱不同")
    print(yanzhengma1)
    print(VCode)
    if yanzhengma1!=VCode:
        return HttpResponse("验证码错误")
    return HttpResponse("验证成功")

def forgetandchangepassword(request):

    return render(request,'forgetandchangepassword.html')

def random_str(randomlength=6):#create the Verification Code
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def text(request):
    return render(request,'text.html')