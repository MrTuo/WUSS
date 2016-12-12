# coding=utf-8
"""
Django settings for WUSS project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'io5x9=2ror04istxc^o!95w(er+gu7c9$39=ah=e!@n2!b_wri'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DEFAULT_CHARSET = 'utf-8'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Myuser',
    'update_manage',
    'url_manage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WUSS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WUSS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

TEMPLATE_DIRS=(
        './Myuser/templates/',
        './update_manage/templates',
)
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#定义@login require跳转链接
LOGIN_URL = '/homepage'

# #定义Email信息-新浪smtp
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.sina.com'            #SMTP服务器
EMAIL_PORT = 25                        #SMTP服务器端口
EMAIL_HOST_USER = 'qq519043202@sina.com'    #用户名
EMAIL_HOST_PASSWORD = 'qq963852741'#第三方邮件收发授权码

#定义Email信息-网易smtp
# EMAIL_USE_TLS = False
# EMAIL_HOST = 'smtp.163.com'            #SMTP服务器
# EMAIL_PORT = 25                        #SMTP服务器端口
# EMAIL_HOST_USER = 'wussapp@163.com'    #用户名
# EMAIL_HOST_PASSWORD = 'wussapp20162016'#第三方邮件收发授权码

# 缓存设置
CACHE_COUNT = 30 # 最大缓存文件数量
CACHE_FQ = 30*60 # 缓存频率,单位：秒
CACHE_PATH = os.path.join(BASE_DIR, 'cache/').replace('\\','/')  # 缓存文件路径
