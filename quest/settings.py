"""
Django settings for quest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os.path
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1d=*_25ru__x@g#itxjy#ixld7(!(r@(x4_5-_6!4s7mzf-u$q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
LANGUAGES = (
    ('en', 'English'),
    )


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'transmeta',
    'questionnaire',
    'questionnaire.page',
    'django_cas',

)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django_cas.middleware.CASMiddleware', 
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'questionnaire.request_cache.RequestCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

STATICFILES_DIR=(

    os.path.abspath('./ed-questionnaire/questionnaire/static/'),
    os.path.abspath('./static'),
  
    )

TEMPLATE_DIRS=(
    os.path.abspath('./ed-questionnaire/questionnaire/templates'),
    os.path.abspath('./templates'),
    )

STATIC_ROOT='./static'

MEDIA_ROOT = BASE_DIR +'/media'

ROOT_URLCONF = 'quest.urls'

WSGI_APPLICATION = 'quest.wsgi.application'

AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend', 
'django_cas.backends.CASBackend',
)

CAS_SERVER_URL='http://cas-test.its.hawaii.edu/cas/login'
CAS_REDIRECT_URL='http://localhost:8000'
CAS_VERSION='2'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'quest.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

SITE_ID = 1

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
