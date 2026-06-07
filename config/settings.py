"""
Django settings for AI Travel Assistant project.
"""
import os
from pathlib import Path

from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-change-me-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'crispy_forms',
    'crispy_bootstrap5',
    # Local apps
    'accounts.apps.AccountsConfig',
    'translations.apps.TranslationsConfig',
    'phrasebook.apps.PhrasebookConfig',
    'dashboard.apps.DashboardConfig',
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
        'DIRS': [BASE_DIR / 'templates'],
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

# PostgreSQL Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='travel_assistant_db'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='postgres'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard:home'
LOGOUT_REDIRECT_URL = 'accounts:login'

# Crispy Forms with Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Supported languages for the translation interface (100+ languages)
SUPPORTED_LANGUAGES = [
    ('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'),
    ('hy', 'Armenian'), ('az', 'Azerbaijani'), ('eu', 'Basque'), ('be', 'Belarusian'),
    ('bn', 'Bengali'), ('bs', 'Bosnian'), ('bg', 'Bulgarian'), ('ca', 'Catalan'),
    ('ceb', 'Cebuano'), ('ny', 'Chichewa'), ('zh', 'Chinese (Simplified)'),
    ('zh-TW', 'Chinese (Traditional)'), ('co', 'Corsican'), ('hr', 'Croatian'),
    ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'),
    ('eo', 'Esperanto'), ('et', 'Estonian'), ('tl', 'Filipino'), ('fi', 'Finnish'),
    ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('ka', 'Georgian'),
    ('de', 'German'), ('el', 'Greek'), ('gu', 'Gujarati'), ('ht', 'Haitian Creole'),
    ('ha', 'Hausa'), ('haw', 'Hawaiian'), ('he', 'Hebrew'), ('hi', 'Hindi'),
    ('hmn', 'Hmong'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('ig', 'Igbo'),
    ('id', 'Indonesian'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'),
    ('jw', 'Javanese'), ('kn', 'Kannada'), ('kk', 'Kazakh'), ('km', 'Khmer'),
    ('ko', 'Korean'), ('ku', 'Kurdish'), ('ky', 'Kyrgyz'), ('lo', 'Lao'),
    ('la', 'Latin'), ('lv', 'Latvian'), ('lt', 'Lithuanian'), ('lb', 'Luxembourgish'),
    ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'),
    ('mt', 'Maltese'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mn', 'Mongolian'),
    ('my', 'Myanmar (Burmese)'), ('ne', 'Nepali'), ('no', 'Norwegian'), ('or', 'Odia'),
    ('ps', 'Pashto'), ('fa', 'Persian'), ('pl', 'Polish'), ('pt', 'Portuguese'),
    ('pa', 'Punjabi'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sm', 'Samoan'),
    ('gd', 'Scots Gaelic'), ('sr', 'Serbian'), ('st', 'Sesotho'), ('sn', 'Shona'),
    ('sd', 'Sindhi'), ('si', 'Sinhala'), ('sk', 'Slovak'), ('sl', 'Slovenian'),
    ('so', 'Somali'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili'),
    ('sv', 'Swedish'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('te', 'Telugu'),
    ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'),
    ('ug', 'Uyghur'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('cy', 'Welsh'),
    ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu'),
]
