from django.apps import AppConfig


class RegistrationSystemConfig(AppConfig):
    name = 'registration_system'

    def ready(self):
        import registration_system.signals
