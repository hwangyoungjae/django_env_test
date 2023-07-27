from django.apps import AppConfig

from .injection import injection_configuration


class ConfigurationConfig(AppConfig):
    name = 'configuration'

    def ready(self) -> None:
        injection_configuration()
