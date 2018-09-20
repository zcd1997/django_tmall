

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#把apps添加到
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

SECRET_KEY = '^16+^#dni#@d)$y+7b!5uyu!qz)orv*cwhl2l*0siqms=sta*j'

DEBUG = True

ALLOWED_HOSTS = []

#系统内置app
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',]
#第三方app
EXT_APPS = [
    #xadmin模块
    'xadmin',
    'crispy_forms',
    #主题模块
    'reversion',]
#自定义APP
MY_APPS =[
    #首页
    'apps.home',
    #用户模块
    'apps.user',
    #分类详情模块
    'apps.cate_detail',
    #购物车模块
    'apps.shop_car',
    #商品详情模块
    'apps.shop_detail',
    #订单模块
    'apps.shop_order',
    #支付模块
    'apps.shop_pay',
    #搜索模块
    'apps.search'
]

INSTALLED_APPS = SYS_APPS + EXT_APPS +MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_tmall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'apps.user.context_processors.shop_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_tmall.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_tmall',
        'USER':'root',
        'PASSWORD':'123456',

    }
}

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



LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#配置静态资源目录
STATIC_URL = '/static/'

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

#配置多媒体资源目录
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')


#全局跳转登录地址

LOGIN_URL = 'user/login/'