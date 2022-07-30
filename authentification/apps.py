"""module to authentificate user  """

from django.apps import AppConfig


class AuthentificationConfig(AppConfig):

    """class to authentificate user"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentification'
