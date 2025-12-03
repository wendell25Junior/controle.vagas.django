from django.apps import AppConfig


class MonitoramentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitoramento'

    def ready(self):
        import monitoramento.signals
        