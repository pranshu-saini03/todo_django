from accounts.models import User, Permission

def has_permission(user_id, action):
    user = User.objects.get(id=user_id)
    perm = Permission.objects.get(role=user.role)
    return getattr(perm, action)
