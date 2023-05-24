from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application'

    # def ready(self):
    #     from .add_utils.csv import import_csv_to_database
    #     try:
    #         import_csv_to_database('uszips.csv')
    #     except:
    #         ...
