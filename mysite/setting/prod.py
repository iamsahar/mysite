from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#dp#3ocj21)7vy980809oi0ae!heu^+7jmn3@&(4ao^9%d5)(v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['imsahar.ir', 'www.imsahar.ir']

# sites framework
SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'imsahari_travel',
        'USER': 'imsahari_admin',
        'PASSWORD': 'PZDn]Rm#kM0o',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = '/home/imsahari/public_html/static'
MEDIA_ROOT = '/home/imsahari/public_html/media'
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE =True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True

## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

