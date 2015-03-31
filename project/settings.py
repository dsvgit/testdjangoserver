"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os 
import ldap3
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '52rp5z-cp4h0wffq3e9z0y6weic_3eyuxjsk(y*m%80e12&kdh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'loginsys',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_remote_auth_ldap.middleware.RemoteUserMiddleware', #for ldap
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/opt/myenv/project/static/'

#изменяем класс, работающий с авторизацией
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
#    'loginsys.auth_backends.CustomUserModelBackend',
#    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
    LDAPSearch("ou=admin,dc=test,dc=com", ldap3.SCOPE_SUBTREE, "(uid=%(user)s)"),
    LDAPSearch("ou=superadmin,dc=test,dc=com", ldap3.SCOPE_SUBTREE, "(uid=%(user)s)"),
)

#изменяем класс для работы с пользователями
#CUSTOM_USER_MODEL = 'loginsys.CustomUser'
#UTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
# Обязательный 
#AUTH_LDAP_SERVER =  '188.166.9.61/phpldapadmin/'                        # Имя хоста 
#AUTH_LDAP_BASE_USER =  "CN = admin, DC = test, DC = com"    # административного пользователя Имя пользователя 
##AUTH_LDAP_BASE_PASS =  "admin"                      # административного пользователя Пароль 
#AUTH_LDAP_BASE_DN =  "DC = test, DC = com"               # Base DN (также принимает O = example.com формат) 
#AUTH_LDAP_FIELD_DOMAIN =  "example.com"                # домена, с которого пользователи будут принимать домен для манекена поколения электронной почты (он держит Django счастливы!) 
#AUTH_LDAP_GROUP_NAME =  "superadmin"                  # Django группу для пользователей LDAP (помогает нам управлять ими для смены пароля и т.д.) 
#AUTH_LDAP_VERSION =  3                                 # LDAP версии 
#AUTH_LDAP_OLDPW =  False                               # сервер может взять старую пароль? Верно / Неверно 