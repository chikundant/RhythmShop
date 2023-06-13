from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'tailwind',
    'theme',
    'ckeditor',
    'django_browser_reload',
    'home.apps.HomeConfig',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'contact_us.apps.ContactUsConfig',
    'users.apps.UsersConfig',
    'django.contrib.postgres',

]
AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'rhythm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'rhythm.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': os.environ.get('DB_DATABASE_NAME', default=BASE_DIR / 'db.sqlite3'),
        'USER':  os.environ.get('DB_USER', default='user'),
        'HOST':  os.environ.get('DB_HOST', default='localhost'),
        'PASSWORD':  os.environ.get('DB_PASSWORD', default='password'),
        'PORT':  os.environ.get('DB_HOST', default='5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'  # джанго ищет все пути стати на момент разработки
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'theme/static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    "127.0.0.1",
]

TAILWIND_APP_NAME = 'theme'

NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'

CKEDITOR_UPLOAD_PATH = "uploads/"

CART_SESSION_ID = 'cart'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

REDIS_HOST = 'redis'
REDIS_PORT = '6379'

CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTION = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
