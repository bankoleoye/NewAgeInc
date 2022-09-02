from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AuthenticationAPI'
    verbose_name = _('AuthenticationAPI')

