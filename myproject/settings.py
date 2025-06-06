"""
Django settings for myproject project.
Generated by 'django-admin startproject' using Django 4.2.15.
"""

from pathlib import Path
import os

# 项目根目录路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔧 通过环境变量判断是否处于生产环境
IS_PROD = os.getenv("DJANGO_PROD", "0") == "1"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ds$+u2h_eds$@%=az33yz4s02siky4tt5h#izbx(^d)=i08m62'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_PROD

ALLOWED_HOSTS = ['lab-li.ciim-hannover.de', '127.0.0.1', 'localhost']

# 设置 SCRIPT_NAME 前缀，仅在部署时使用
FORCE_SCRIPT_NAME = '/mb-granuloma' if IS_PROD else ''
USE_X_FORWARDED_HOST = IS_PROD

# 自动处理 STATIC_URL（用于模板和静态资源路径）
STATIC_URL = f"{FORCE_SCRIPT_NAME}/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# 应用定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact',
    'dataview1',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ⚠️ 确保这一行存在
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 自定义路径
MY_ANNDATA_DIR = BASE_DIR / "data" / "Splited_data_for_webtool"

# 密码验证
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 国际化
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 默认主键类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 允许跨域访问的前端地址（如果用 Vue/React 开发）
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]

