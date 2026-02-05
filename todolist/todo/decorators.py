from functools import wraps
from django.http import JsonResponse

def class_permission(*permissions):

    def decorator(view_class):
        original_dispatch = view_class.dispatch

        @wraps(original_dispatch)
        def new_dispatch(self, request, *args, **kwargs):

            for perm in permissions:
                if not perm(request):

                    if perm.__name__ == "is_jwt_authenticated":
                        return JsonResponse(
                            {"error": "Unauthorized"},
                            status=401
                        )
                    return JsonResponse(
                        {"error": "Permission denied"},
                        status=403
                    )

            return original_dispatch(self, request, *args, **kwargs)

        view_class.dispatch = new_dispatch
        return view_class

    return decorator

