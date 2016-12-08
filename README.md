# 软工大作业-WUSS (Web update subscription system) 说明文档
## 项目简介
WUSS系统是一个网页更新订阅系统。用户可以对自己感兴趣的URL进行订阅，系统定时自动追踪这也页面的更新（识别页面内容的变化），并把更新内容加以提取，通过email或者手机短信推送至用户。

## 现实意义
- 可以让用户第一时间内获得自己希望获得的信息
- 节约了用户不断访问页面来判断消息是否更新的时间，给用户更多的自由时间，只需要等待网站自动发送的消息即可
- 替用户记得重要信息，避免用户因为繁忙的工作而忘记自己希望获得的信息

## 功能清单
- 用户登录界面，获得用户提供的消息提供渠道（例如email、QQ、手机短信）以及用户的身份信息（不需要身份证之类的，只需要职业，兴趣等方面的信息）
- 支持用户对所关注网页URL进行增删改管理，也可暂停/重启已追踪的 网页URL；
- 根据用户的个人信息提供用户可能感兴趣的URL，让用户选择是否追踪
- 针对用户关注的全部网页URL，每天特定时间(如20:00)将它们在本日内的全部更新汇聚起来推送给订阅用户	

## 系统体系结构
- 网页更新订阅系统
	- 登录模块、
		- 登录
		- 注册
		- 信息管理（密码修改，密码找回，用户信息修改）
	- URL管理模块
		- 添加URL
		- 删除URL
		- 修改URL
	- 更新订阅管理模块
		- 更新判断
		- 推送

## 技术支持
Python3 + Django1.10

## 本地安装
- 同步项目到本地后，cd到WUSS/WUSS目录下，依次运行以下命令
	- python manage.py makemigrations
	- python manage.py migrate

- 然后创建超级用户
	- python manage.py createsuperuser

- 依次输入账号密码后，就能开始运行了
	- python manage.py runserver

- 在浏览器输入127.0.0.1:8000访问

- 其他问题
	- 使用python2.7，需要在几处代码做相应修改
		- 在WUSS/WUSS/wsgi.py中，将import _thread 改为 thread，文件中其他地方也做相应修改
		- 在WUSS/updage_manage/views.py中将print的括号去掉
	- 可能需要安装的其他包，由于大家python包都不一样，我列出几个可能缺少的，其他的自己安装吧，建议使用pip
		- feedparser（解析RSS的包）
		- beautifulsoap（python著名的爬虫框架）
	- 订阅推送的邮件发送方是在163申请的，登录账号密码如下：（注：登录密码和第三方发送密码不同）。当然，你可以在WUSS/WUSS/settings.py中修改为你的邮箱。
		- wussapp@163.com/wussapp2016

## 关于我们
任何问题可以联系邮箱：
- tuomingxiang@gmail.com（MrTuo负责订阅模块实现）
- 501874997@qq.com（Arnold负责整个网站前端以及用户模块实现）
- zengxuwei9595@qq.com（Aloey负责URL管理模块实现）


