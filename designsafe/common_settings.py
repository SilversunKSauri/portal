"""
Django settings for designsafe project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '__CHANGE_ME_!__')

SESSION_COOKIE_DOMAIN = os.environ.get('SESSION_COOKIE_DOMAIN')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'cmsplugin_cascade',
    'cmsplugin_cascade.extra_fields',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'djangocms_style',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_forms',

    'pipeline',
    'filer',
    'reversion',
    'bootstrap3',
    'termsandconditions',
    'impersonate',

    # custom
    'designsafe.apps.tas',
    # 'designsafe.apps.cilogon',
    'designsafe.apps.cms_plugins',
)

AUTHENTICATION_BACKENDS = (
    'designsafe.apps.tas.backends.TASBackend',
    # 'designsafe.apps.cilogon.backends.CILogonBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'designsafe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'designsafe', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'designsafe.context_processors.analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'designsafe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if os.environ.get('DATABASE_HOST'):
    # mysql connection
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': os.environ.get('DATABASE_PORT'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en-us', 'English'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/designsafe-ci.org/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'designsafe', 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

MEDIA_ROOT = '/var/www/designsafe-ci.org/media/'
MEDIA_URL = '/media/'

CMS_TEMPLATES = (
    ('cms_page.html', 'Basic Page'),
)

CMSPLUGIN_CASCADE_PLUGINS = (
    'cmsplugin_cascade.bootstrap3',
    'cmsplugin_cascade.link',
)

CMSPLUGIN_CASCADE_ALIEN_PLUGINS = (
    'TextPlugin',
    'StylePlugin',
    'FilerImagePlugin',
    'FormPlugin',
    'MeetingFormPlugin',
    'ResponsiveEmbedPlugin',
)

MIGRATION_MODULES = {
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
}

DJANGOCMS_FORMS_PLUGIN_MODULE = 'Generic'
DJANGOCMS_FORMS_PLUGIN_NAME = 'Form'
DJANGOCMS_FORMS_TEMPLATES = (
    ('djangocms_forms/form_template/default.html', 'Default'),
)
DJANGOCMS_FORMS_USE_HTML5_REQUIRED = False
DJANGOCMS_FORMS_WIDGET_CSS_CLASSES = {
    'text': ('form-control', ),
    'textarea': ('form-control', ),
    'email': ('form-control', ),
    'number': ('form-control', ),
    'phone': ('form-control', ),
    'url': ('form-control', ),
    'select': ('form-control', ),
    'file': ('form-control', ),
    'date': ('form-control', ),
    'time': ('form-control', ),
    'password': ('form-control', ),
}
DJANGOCMS_FORMS_DATETIME_FORMAT = '%d-%b-%Y %H:%M'

#####
#
# Bootstrap3 Settings
#
#####
BOOTSTRAP3 = {
    'required_css_class': 'required',
}


#####
#
# Django Impersonate
#
#####
IMPERSONATE_REQUIRE_SUPERUSER = True


#####
#
# Logger config
#
#####
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s %(name)s.%(funcName)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'designsafe': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'meetings': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'tas': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('SMTP_HOST', 'localhost')
EMAIL_PORT = os.environ.get('SMTP_PORT', 25)
EMAIL_HOST_USER = os.environ.get('SMTP_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('SMTP_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'no-reply@designsafe-ci.org')
MEETING_REQUEST_EMAIL = os.environ.get('MEETING_REQUEST_EMAIL', 'info@designsafe-ci.org')


###
# Pipeline
#
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.slimit.SlimItCompressor'

PIPELINE_CSS = {
    'vendor': {
        'source_filenames': (
          'vendor/bootstrap-ds/css/bootstrap.css',
          # 'vendor/bootstrap-ds/css/bootstrap-theme.css',
          'vendor/bootstrap-datepicker/dist/css/bootstrap-datepicker3.css',
        ),
        'output_filename': 'css/vendor.css',
    },
    'main': {
        'source_filenames': (
          'styles/main.css',
        ),
        'output_filename': 'css/main.css',
    },
}

PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
            'vendor/modernizer/modernizr.js',
            'vendor/jquery/dist/jquery.js',
            'vendor/bootstrap-ds/js/bootstrap.js',
            'vendor/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js',
        ),
        'output_filename': 'js/vendor.js',
    },
    'main': {
        'source_filenames': (
            'scripts/utils.js',
            'scripts/dateinput.js',
            'scripts/navbar.js',
        ),
        'output_filename': 'js/main.js',
    },
}

###
# Opbeat Integration
#
if os.environ.get('OPBEAT_ORGANIZATION_ID'):
    INSTALLED_APPS += (
        'opbeat.contrib.django',
    )
    OPBEAT = {
        'ORGANIZATION_ID': os.environ.get('OPBEAT_ORGANIZATION_ID', ''),
        'APP_ID': os.environ.get('OPBEAT_APP_ID', ''),
        'SECRET_TOKEN': os.environ.get('OPBEAT_SECRET_TOKEN', ''),
    }
    MIDDLEWARE_CLASSES = (
        'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    ) + MIDDLEWARE_CLASSES
