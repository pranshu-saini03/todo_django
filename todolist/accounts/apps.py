from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self):
        from .services.rbac_service import setup_roles_and_permissions
        setup_roles_and_permissions()