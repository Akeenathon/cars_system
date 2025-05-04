from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self):
        # Importando o módulo de sinais para garantir que os sinais sejam registrados
        import cars.signals
