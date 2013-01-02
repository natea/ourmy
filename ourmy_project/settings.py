# Django settings for ourmy project.

import os
from os import environ

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

def rel(*x):
    return os.path.join(PROJECT_ROOT, *x)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ourmy.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# When the @login_required decorator is used, this is where django will send unregistered users
LOGIN_URL = '/login/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = (os.path.join(PROJECT_ROOT, "media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = (os.path.join(PROJECT_ROOT, "static"))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    (os.path.join(PROJECT_ROOT, 'media')),
    # (os.path.join(PROJECT_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5usz#82h*80(b64mc#nei1!utdh8tr41-k+vgr!c#%5o=2+@%_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'singly.backends.SinglyBackend',
# )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'ourmy_project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ourmy_project.wsgi.application'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'singly',
    'bootstrap_toolkit',
    'test_bootstrap',
    'south',
    'debug_toolbar',
    'ourmy_app',
    'sharing',
)

# Bit.ly API credentials go here.
BITLY_LOGIN = "ourmy"
BITLY_API_KEY = "R_d0e270b20075dbb971f660c0fad3f5ce"

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,       # this will show a "you are being redirected" page you must click through on redirects
    # 'SHOW_TOOLBAR_CALLBACK': None,      # you can pass a function that determines whether to show the toolbar
    # 'EXTRA_SIGNALS': ['myproject.signals.MySignal'],    # An array of custom signals that might be in your project, defined as the python path to the signal.
    # 'HIDE_DJANGO_SQL': False,           # If True (the default) then code in Django itself won't be shown in SQL stacktraces.
    # 'SHOW_TEMPLATE_CONTEXT': True       # If True (the default) then a template's context will be included with it in the Template debug panel.
    # 'TAG': 'div',                       # If set, this will be the tag to which debug_toolbar will attach the debug toolbar. Defaults to 'body'.
    # 'ENABLE_STACKTRACES' : True,        # If True (default) this will show stacktraces for SQL queries and cache calls.
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

BOOTSTRAP_BASE_URL      = 'http://twitter.github.com/bootstrap/assets/'
BOOTSTRAP_CSS_BASE_URL  = BOOTSTRAP_BASE_URL + 'css/'
BOOTSTRAP_CSS_URL       = BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
BOOTSTRAP_JS_BASE_URL   = BOOTSTRAP_BASE_URL + 'js/'
# Enable for single bootstrap.js file
#BOOTSTRAP_JS_URL        = BOOTSTRAP_JS_BASE_URL + 'bootstrap.js'

SINGLY_CLIENT_ID="26c38ca03b256c31720cc9cd8ebec776"
SINGLY_CLIENT_SECRET="b174c23ac692e1d0e920e92798ec34c8"
# lvh.me is just a domain name for localhost
#SINGLY_REDIRECT_URI = 'http://lvh.me:8000/authorize/callback'
SINGLY_REDIRECT_URI = 'http://localhost:8000/authorize/callback'

AUTH_PROFILE_MODULE = "singly.SinglyProfile"

if environ.get("RACK_ENV", None) == "production":
    import dj_database_url
    
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
    INSTALLED_APPS += ("gunicorn",)
    # from http://offbytwo.com/2012/01/18/deploying-django-to-heroku.html
    # To make it easier to turn DEBUG on and off consider adding the following to your settings.py:
    DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
    TEMPLATE_DEBUG = DEBUG
    # Now you can turn debug on using heroku config:add DJANGO_DEBUG=true and turn it off with heroku config:remove DJANGO_DEBUG

    # EMAIL_HOST = 'smtp.sendgrid.net'
    # EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    # EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    # EMAIL_PORT = 587        # 25, 587, 2525 and 465 on ssl
    # EMAIL_USE_TLS = True  

    AWS_ACCESS_KEY_ID = 'AKIAJ5HGQJW3TIME642Q'  #  os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = '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'  #  os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = 'ourmy-files'

    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'