from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-lk^s4jma29my=_9)n727)hmked0e5ukr-y_48^8%+%am^#q@_g'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'socialnetwork',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'newpassword'
    }
}