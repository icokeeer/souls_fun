from .base import *
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'souls-fun',
        'USER': 'admin',
        'PASSWORD': 'dujitang',
        'HOST': 'thesouls.fun',
        'PORT': '33060',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            'charset': 'utf8'
        }
    }
}

STATIC_ROOT = '../../static'
