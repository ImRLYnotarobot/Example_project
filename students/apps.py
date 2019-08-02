from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'
    verbose_name = 'Students application'

    def ready(self):
        import students.signals
