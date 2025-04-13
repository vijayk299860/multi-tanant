# Import all settings from base.py
from config.settings.base import *
import os

# Debug settings
DEBUG = False
TEMPLATE_DEBUG = False

# Multi-database configuration for production
DATABASES = {
    'default': {  # Management database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('MGMT_DB_NAME', 'saas_management_prod'),
        'USER': os.environ.get('MGMT_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('MGMT_DB_PASSWORD'),
        'HOST': os.environ.get('MGMT_DB_HOST', 'localhost'),
        'PORT': os.environ.get('MGMT_DB_PORT', '5432'),
        'CONN_MAX_AGE': 60,  # Keep connections alive for 60 seconds
        'OPTIONS': {
            'sslmode': 'require',  # Require SSL connection in production
        }
    },
    'tenant1': {  # First tenant database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TENANT1_DB_NAME', 'saas_tenant1_prod'),
        'USER': os.environ.get('TENANT1_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('TENANT1_DB_PASSWORD'),
        'HOST': os.environ.get('TENANT1_DB_HOST', 'localhost'),
        'PORT': os.environ.get('TENANT1_DB_PORT', '5432'),
        'CONN_MAX_AGE': 60,
        'OPTIONS': {
            'sslmode': 'require',
        }
    },
    'tenant2': {  # Second tenant database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TENANT2_DB_NAME', 'saas_tenant2_prod'),
        'USER': os.environ.get('TENANT2_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('TENANT2_DB_PASSWORD'),
        'HOST': os.environ.get('TENANT2_DB_HOST', 'localhost'),
        'PORT': os.environ.get('TENANT2_DB_PORT', '5432'),
        'CONN_MAX_AGE': 60,
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}

# Database router to direct queries to the appropriate database
DATABASE_ROUTERS = ['apps.tenants.router.TenantDatabaseRouter']

# Security settings
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST', 'example.com'), '*.example.com']  # Allow main domain and subdomains
SECRET_KEY = os.environ.get('SECRET_KEY')  # Get from environment variable

# Security middleware and settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Email configuration for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Caching configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('CACHE_LOCATION', '127.0.0.1:11211'),
    }
}

# Static and media files - consider using a CDN in production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django-errors.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {  # Custom logger for our apps
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Tenant settings
TENANT_DOMAIN_SUFFIX = os.environ.get('TENANT_DOMAIN_SUFFIX', '.example.com')
