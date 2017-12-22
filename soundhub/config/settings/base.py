"""
Django settings for soundhub project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 루트 경로
ROOT_DIR = os.path.dirname(BASE_DIR)
# 기밀정보 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secrets')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')

# 미디어 파일 설정
MEDIA_ROOT = os.path.join(ROOT_DIR, 'temp')

# 스테틱 파일 설정
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

# 기본 프로필 이미지 경로
DEFAULT_IMAGE_PATH = 'default-profile.png'

# S3 저장소 설정
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'

# AWS S3 Access
config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

# Django Mail Information
# EMAIL_HOST_USER 와 PASSWORD 는 config_secret 모듈에서 관리한다
# config_secret 모듈은 import 하기 쉽도록 파이썬 모듈로 관리, .gitignore 에 추가해두었다
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config_secret['email']['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config_secret['email']['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = 'joo2theeon@gmail.com'

FACEBOOK_APP_ID = config_secret['facebook']['FACEBOOK_APP_ID']
FACEBOOK_APP_SECRET_CODE = config_secret['facebook']['FACEBOOK_APP_SECRET_CODE']

# Encryption Key
ENCRYPTION_KEY = config_secret['encrypt']['ENCRYPTION_KEY']

# Django REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config_secret['django']['SECRET_KEY']

RAVEN_CONFIG = {
    'dsn': 'https://e01ad1cebe374afba306dd30c0c95aec:f188b0f719e24508946c5ab72b4de3c8@sentry.io/259770',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

ALLOWED_HOSTS = [
    'localhost',
    '.ap-northeast-2.elasticbeanstalk.com',
    '.che1.co.kr',
    'testserver',
]

AUTH_USER_MODEL = 'users.User'
# 기본 인증 백엔드에 Facebook Backend 추가함
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.FacebookBackend',
]

# Application definition
INSTALLED_APPS = [
    # 빌트인 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 써드파티 앱
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'storages',
    'django_filters',
    'raven.contrib.django.raven_compat',

    # 커스텀 앱
    'users',
    'utils',
    'posts',
    'homepages',
    'direct_messages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


