"""Application configuration for 'base' app."""

from django.apps import AppConfig


class BaseConfig(AppConfig):
    """
    Configuration for 'base' app.

    Args:
        AppConfig (class): Django's base app configuration class.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
