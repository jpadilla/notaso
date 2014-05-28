import os

from configurations import Configuration, values


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ENVIRONMENT = values.Value(environ_prefix=None, default='DEVELOPMENT')

    SECRET_KEY = values.SecretValue(environ_prefix=None)

    DEBUG = values.BooleanValue(False)

    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ALLOWED_HOSTS = [
        'notaso.herokuapp.com',
        'www.notaso.com',
        'notaso.com',
    ]

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',

        # Third Party
        'south',
        'debug_toolbar',
        'django_extensions',
        'storages',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',
        'allauth.socialaccount.providers.twitter',
        'djangosecure',
        'import_export',
        'raven.contrib.django.raven_compat',
        'rest_framework',
        'rest_framework_swagger',

        # Apps
        'notaso.home',
        'notaso.users',
        'notaso.universities',
        'notaso.professors',
        'notaso.departments',
        'notaso.comments',
        'notaso.search',
    )

    MIDDLEWARE_CLASSES = (
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    # Rest Framework Settings
    REST_FRAMEWORK = {
        'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

        # 'DEFAULT_PERMISSION_CLASSES': (
        #     'rest_framework.permissions.IsAuthenticated',
        # ),
        'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        )
    }

    # Swagger Rest Framework Doc Settings
    SWAGGER_SETTINGS = {
        "exclude_namespaces": [],
        "api_version": '0.1',
        "api_path": "/",
        "enabled_methods": [
            'get',
            # 'post',
            # 'put',
            # 'patch',
            # 'delete'
        ],
        "api_key": '',
        "is_authenticated": False,
        "is_superuser": False,
    }

    ROOT_URLCONF = 'notaso.urls'

    WSGI_APPLICATION = 'notaso.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'storage.sqlite3')))

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/
    STATIC_ROOT = 'assets'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",

        # allauth specific context processors
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
    )

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        "django.contrib.auth.backends.ModelBackend",

        # `allauth` specific authentication methods, such as login by e-mail
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    SITE_ID = 1

    AUTH_USER_MODEL = 'users.User'

    # auth and allauth settings
    LOGIN_REDIRECT_URL = '/'
    LOGIN_URL = '/accounts/login/'
    ACCOUNT_EMAIL_VERIFICATION = "none"
    ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Notaso] '
    ACCOUNT_LOGOUT_ON_GET = True
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
    ACCOUNT_USERNAME_BLACKLIST = ['admin']
    ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
    ACCOUNT_SIGNUP_FORM_CLASS = 'notaso.users.forms.SignupForm'
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_USERNAME_REQUIRED = False

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DEFAULT_FROM_EMAIL = values.Value()
    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.IntegerValue()
    EMAIL_USE_TLS = values.BooleanValue(False)

    CAMO_URL = values.Value(environ_prefix=None)
    CAMO_KEY = values.Value(environ_prefix=None)


class Development(Common):
    DEBUG = True

    TEMPLATE_DEBUG = DEBUG

    PROTOCOL = 'http'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Dummy cache for development
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


class Production(Common):
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    # django-secure settings
    PROTOCOL = 'https'
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATIC_URL = 'https://com-notaso-static.s3.amazonaws.com/'
    MEDIA_URL = STATIC_URL

    AWS_PRELOAD_METADATA = True
    AWS_ACCESS_KEY_ID = values.Value(environ_prefix=None)
    AWS_SECRET_ACCESS_KEY = values.Value(environ_prefix=None)
    AWS_STORAGE_BUCKET_NAME = values.Value(environ_prefix=None)
