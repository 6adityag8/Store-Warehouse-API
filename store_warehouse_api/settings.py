import secrets
from pathlib import Path

import environ

# Reading .env file
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default=secrets.token_hex(24))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

# Please specify comma-separated string in .env file
ALLOWED_HOSTS = env.str('ALLOWED_HOSTS', default='*').split()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'warehouse',
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

ROOT_URLCONF = 'store_warehouse_api.urls'

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

WSGI_APPLICATION = 'store_warehouse_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'db_store': {
        'ENGINE': env.str('DB_STORE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.str('DB_STORE_NAME', default=BASE_DIR / 'db_store.sqlite3'),
        'USER': env.str('DB_STORE_USER', default=''),
        'PASSWORD': env.str('DB_STORE_PASSWORD', default=''),
        'HOST': env.str('DB_STORE_HOST', default=''),
        'PORT': env.str('DB_STORE_PORT', default=''),
    },
    'db_warehouse': {
        'ENGINE': env.str('DB_WAREHOUSE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.str('DB_WAREHOUSE_NAME', default=BASE_DIR / 'db_warehouse.sqlite3'),
        'USER': env.str('DB_WAREHOUSE_USER', default=''),
        'PASSWORD': env.str('DB_WAREHOUSE_PASSWORD', default=''),
        'HOST': env.str('DB_WAREHOUSE_HOST', default=''),
        'PORT': env.str('DB_WAREHOUSE_PORT', default=''),
    },
}

DATABASE_ROUTERS = ['store_warehouse_api.router.DBRouter']

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
