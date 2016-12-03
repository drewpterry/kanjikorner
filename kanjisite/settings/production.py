from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.kanjisama.com',
                '.kanjisama.com.']

ADMINS = (('Drew', 'drewpterry@yahoo.com'),)
SERVER_EMAIL = os.environ['SERVER_EMAIL']

EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PW']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_EMAIL']
