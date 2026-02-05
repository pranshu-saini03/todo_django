# services/rbac_service.py
from ..models import Role, Permission
from ..rbac_config import ROLES


def setup_roles_and_permissions():
    for role_name, perms in ROLES.items():

        role=Role.objects.get_or_create(name=role_name)

        Permission.objects.update_or_create(
            role=role[0],
            defaults={
                "can_create": perms["can_create"],
                "can_read": perms["can_read"],
                "can_update": perms["can_update"],
                "can_delete": perms["can_delete"],
            }
        )
