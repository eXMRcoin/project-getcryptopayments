from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'exmr',
        'USER': 'postgres',
        'PASSWORD': 'nV4DS3p2',
        'HOST': 'localhost',
    }
}


# For email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True

EMAIL_HOST = 'e12.ehosts.com'

EMAIL_HOST_USER = 'noreply@getcryptopayments.net'

EMAIL_HOST_PASSWORD = 'Gcp1234!!'

EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'exmr.test@gmail.com'
# EMAIL_HOST_PASSWORD = 'Adminqwerty123'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEBUG = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = (
   ('ME', 'anandkrishnan.techversant@gmail.com'),
)
MANAGERS = ADMINS
