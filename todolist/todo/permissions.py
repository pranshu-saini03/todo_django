from accounts.models import User, Permission


def is_jwt_authenticated(request):
  

    return hasattr(request, "user_id")

def has_permission(user_id, action):
    """
    Checks whether a user (by user_id) has a given permission action
    like: can_create, can_read, can_update, can_delete
    """
    try:
        user = User.objects.get(id=user_id)
        perm = Permission.objects.get(role=user.role)
        return bool(getattr(perm, action, False))
    except (User.DoesNotExist, Permission.DoesNotExist):
        return False
def can_create(request):
    return has_permission(request.user_id, "can_create")
def can_read(request):
    return has_permission(request.user_id, "can_read")
def can_update(request):
    return has_permission(request.user_id, "can_update")
def can_delete(request):
    return has_permission(request.user_id, "can_delete")
