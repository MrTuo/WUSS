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

yanzhengma = "000000"
def userhomepage(request):#进入用户页面主页
    if request.user.is_authenticated():
        content = {
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':1,
            'chooise_user_left_nav':1,
        }
        return render(request, 'userhomepage.html', content)
    return HttpResponseRedirect('/error')

def usermanagement(request):#进入用户账号管理页面
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

def urlmanagement(request):#URL管理页面
    if request.user.is_authenticated():
        content={
            'user_is_logic': 'YES',
            'user': request.user,
            'chooise':3,
            'chooise_user_left_nav':1,
        }
        return render(request,'URLmanagement.html',content)
    return HttpResponseRedirect('/error')


def Userjudge(request):#判断是否登录
    if request.user.is_authenticated():
        return HttpResponseRedirect("/userhomepage")
    else:
        return HttpResponseRedirect("/login")

def mainhomepage(request):#进入到主页
    if request.user.is_authenticated():
        content={
            'user_is_logic':'YES'
        }
        return render(request,'homepage1.html',content)
    content={
        'user':'登录'
    }
    return render(request,'homepage1.html',content)

def login(request):#登录
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

def Register(request):#注册
    # if request.user.is_authenticated():  #如果登录了就不用在注册了
    #     return HttpResponseRedirect("/user")
    if request.method == 'POST':
        registname = request.POST.get('idname', '')
        registemail = request.POST.get('idemail', '')
        registpassword = request.POST.get('idpassword', '')

        filterResult = User.objects.filter(username=registname)  # 判断用户是否存在
        filterResultemail = User.objects.filter(email=registemail) #判断email是否存在
        if len(filterResult) > 0 or len(filterResultemail) > 0:
            return render(request, 'error.html')  # 如果存在在这里先跳转到错误页面
        user = User()  # 将用户的资料存入到数据库中
        user.username = registname
        user.set_password(registpassword)
        user.email = registemail
        user.save()
        return HttpResponseRedirect('/logic')
    return render(request, 'Register.html')

def Registerajax(request):#注册页面判断用户是否已经注册了
    name=request.POST['name'].strip()
    try:
        user=User.objects.get(username=name)
    except:
        return HttpResponse("可以使用该用户名")
    return HttpResponse("用户已存在")


def Registerajaxemail(request):#注册页面判断邮箱是否注册过
    email = request.POST['email'].strip()
    try:
        user = User.objects.get(email=email)
    except:
        return HttpResponse("可以使用该邮箱")
    return HttpResponse("邮箱已注册")

def error(request):#错误页面
    return render(request,'error.html')

def changeuser(request):#修改密码
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
def logout(request):#登出
    auth.logout(request)
    return HttpResponseRedirect("/")  # 返回到登录界面



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
    mail_list = ['501874997@qq.com' ,]#这里放入的是收件人
    from_email = settings.EMAIL_HOST_USER#这里放的是发件人
    message = u'用户:' + name + u' 这是测试邮件'
    email_template_name = 'send_email_template.html'#这里是邮件模板
    t = loader.get_template(email_template_name)
    html_content = t.render()
    msg = EmailMultiAlternatives(subject, html_content, from_email, mail_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # send_mail(subject, message, from_email, mail_list)
    return HttpResponseRedirect("/")

emailsend=""#记录发送的email避免更改email
def send_email_to_changepassword(request):
    yanzhengma = random_str()
    email=request.POST['email'].strip()
    emailsend=email
    print(email)
    print(emailsend)
    try:
        user=User.objects.get(email=email)
    except:
        print("herer")
        return HttpResponse("邮箱未注册无法发送")
    subject = u'WUSS用户忘记密码'
    from_email=settings.EMAIL_HOST_USER
    message = u'亲爱的用户:'+ email + "您在WUSS请求的验证码是:"+yanzhengma
    send_mail(subject, message, from_email, [email,])
    return HttpResponse("发送成功")


def forgetpassword(request):#忘记密码
    return render(request,'forget_password.html')

def applyfor(request):
    email = request.POST['email'].strip()
    yanzhengma1=request.POST['yanzhengma'].strip()
    print(email+'1')
    print(emailsend+'2')
    if email!=emailsend:
        return HttpResponse("两次邮箱不同！")
    if yanzhengma!=yanzhengma1:
        return HttpResponse("验证码错误")
    return HttpResponse("验证成功")

def forgetandchangepassword(request):
    return render(request,'forgetandchangepassword.html')

def random_str(randomlength=6):#生成随机验证码
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def text(request):
    return render(request,'text.html')