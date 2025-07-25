"""
HomeCampus Flask Configuration
Python 3.9 migration configuration settings

This works alongside the existing Config.py during the migration phase.
Gradually replace Tipfy config with Flask config as we migrate handlers.
"""

import os
from datetime import timedelta

# Import the existing Tipfy config for backward compatibility
from Config import config as tipfy_config

class FlaskConfig:
    """Flask configuration class for Python 3 migration"""
    
    # Flask core settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'HOMECAMPUS25_AUTH_SECRET_KEY_CHANGE_IN_PRODUCTION')
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None
    
    # Google Cloud settings
    GOOGLE_CLOUD_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT', 'homecampus-dev')
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Application settings
    APP_NAME = 'HomeCampus'
    APP_VERSION = '3.0.0-migration-phase1'
    DEBUG = True  # Will be overridden in production
    
    # Template settings (migrated from Tipfy Jinja2 config)
    TEMPLATES_AUTO_RELOAD = True
    
    # Email settings (for SendGrid migration)
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = 'noreply@homecampus.sg'
    
    # PayPal settings (from original app)
    PAYPAL_MODE = 'sandbox'  # 'sandbox' or 'live'
    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID')
    PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET')
    
    # User model (from Tipfy config)
    USER_MODEL = tipfy_config.get('tipfy.auth', {}).get('user_model', 'Models.HomeCampusUser')

# For development/testing
class DevelopmentConfig(FlaskConfig):
    DEBUG = True
    WTF_CSRF_ENABLED = False  # Easier testing during migration
    
class ProductionConfig(FlaskConfig):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    WTF_CSRF_ENABLED = True
    GOOGLE_CLOUD_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT')

# Configuration selector
config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get configuration based on environment"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config_map.get(env, DevelopmentConfig)