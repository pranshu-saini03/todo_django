from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Todo
from .permissions import has_permission
from accounts.models import User

@csrf_exempt
def add_todo(request):
    if not has_permission(request.user_id, "can_create"):
        return JsonResponse({"error": "Permission denied"}, status=403)

    data = json.loads(request.body)
    user = User.objects.get(id=request.user_id)

    Todo.objects.create(
        user=user,
        title=data.get("title"),
        description=data.get("description")
    )

    request.session["last_action"] = "created todo"

    return JsonResponse({"message": "Todo created"})


@csrf_exempt
def list_todo(request):
    todos = Todo.objects.filter(user_id=request.user_id)
    return JsonResponse({"data": list(todos.values())})


@csrf_exempt
def update_todo(request):
    if not has_permission(request.user_id, "can_update"):
        return JsonResponse({"error": "Permission denied"}, status=403)

    data = json.loads(request.body)
    todo = Todo.objects.get(id=data.get("id"), user_id=request.user_id)

    todo.title = data.get("title", todo.title)
    todo.description = data.get("description", todo.description)
    todo.completed = data.get("completed", todo.completed)
    todo.save()

    return JsonResponse({"message": "Updated"})


@csrf_exempt
def delete_todo(request):
    if not request.user_id:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    if not has_permission(request.user_id, "can_delete"):
        return JsonResponse({"error": "Permission denied"}, status=403)

    data = json.loads(request.body)
    todo_id = data.get("id")

    Todo.objects.get(id=todo_id, user_id=request.user_id).delete()

    return JsonResponse({"message": "Deleted"})
