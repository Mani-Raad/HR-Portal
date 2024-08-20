from django.apps import AppConfig


class EmpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emp_app'


from django.apps import AppConfig

class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee'

    def ready(self):
        import emp_app.signals