from django.apps import AppConfig


class MyAppClass(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyApp'