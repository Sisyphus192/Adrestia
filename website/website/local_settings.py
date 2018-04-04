import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adrestiaDB',
        'USER': 'root',
        'PASSWORD': '961008',
        'HOST': 'localhost',
        'PORT': '3308'
    }
}

DEBUG = True
