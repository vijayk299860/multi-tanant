# Import all settings from base.py
from config.settings.base import *
import os

# Debug settings
DEBUG = True
TEMPLATE_DEBUG = True

# Multi-database configuration for development
DATABASES = {
    'default': {  # Management database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'check_8',
        'USER': 'postgres',
        'PASSWORD': '12345',  
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'tenant1': {  # First tenant database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'check_9',
        'USER': 'postgres',
        'PASSWORD': '12345',  
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'tenant2': {  # Second tenant database
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'check_10',
        'USER': 'postgres',
        'PASSWORD': '12345', 
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Database router to direct queries to the appropriate database
DATABASE_ROUTERS = ['apps.tenants.router.TenantDatabaseRouter']

# Security settings - relaxed for development
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.localhost']  # The .localhost allows subdomains
SECRET_KEY = 'your-development-secret-key'  # In practice, use environment variables

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Development-specific installed apps
INSTALLED_APPS += [
    'debug_toolbar',
]

# Development middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Disable caching in development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# CORS settings for API development
CORS_ALLOW_ALL_ORIGINS = True

# Static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
