# rbac_config.py

ROLES = {
    "admin": {
        "can_create": True,
        "can_read": True,
        "can_update": True,
        "can_delete": True,
    },
    "view": {
        "can_create": False,
        "can_read": True,
        "can_update": False,
        "can_delete": False,
    },
    "user": {
        "can_create": False,
        "can_read": True,
        "can_update": True,
        "can_delete": False,
    }
}
