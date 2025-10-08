from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = [config('PRODUCTION_DOMAIN')] # Here we put domain name for example ['*.your-production-domain.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int) # Usually, 587 for TLS or 465 for SSL
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)  # Set True for TLS (or False for SSL with `EMAIL_USE_SSL=True`)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')