from django.apps import AppConfig


class FeedappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedapp'


    def ready(self):
        try:
            import feedapp.signals  # noqa F401
        except ImportError:
            pass