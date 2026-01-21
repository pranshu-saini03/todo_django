from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import todo


@csrf_exempt
def todo_list(request):
    todo_list = todo.objects.all()
    return JsonResponse(
        {
            "success": True,
            "data": list(todo_list.values())
        },
        status=200
    )


@csrf_exempt
def add_todo(request):
    if request.method != "POST":
        return JsonResponse(
            {"success": False, "message": "Only POST allowed"},
            status=405
        )

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse(
            {"success": False, "message": "Invalid JSON body"},
            status=400
        )

    title = data.get("title")
    description = data.get("description")

    todo_item = todo.objects.create(
        title=title,
        description=description
    )

    return JsonResponse(
        {
            "success": True,
            "message": "Todo created",
            "todo_id": todo_item.id
        },
        status=201
    )


@csrf_exempt
def update_todo(request):
    if request.method != "PUT":
        return JsonResponse(
            {"success": False, "message": "Only PUT allowed"},
            status=405
        )

    todo_id = request.GET.get("int")

    if not todo_id:
        return JsonResponse(
            {"success": False, "message": "Todo id is required"},
            status=400
        )

    try:
        todo_item = todo.objects.get(id=todo_id)
    except todo.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "Todo not found"},
            status=404
        )

    # ✅ safe JSON parsing
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        data = {}

    todo_item.title = data.get("title", todo_item.title)
    todo_item.description = data.get("description", todo_item.description)
    todo_item.completed = data.get("completed", todo_item.completed)

    todo_item.save()

    return JsonResponse(
        {
            "success": True,
            "message": "Todo updated"
        },
        status=200
    )


@csrf_exempt
def delete_todo(request):
    if request.method != "DELETE":
        return JsonResponse(
            {"success": False, "message": "Only DELETE allowed"},
            status=405
        )

    todo_id = request.GET.get("int")

    if not todo_id:
        return JsonResponse(
            {"success": False, "message": "Todo id is required"},
            status=400
        )

    try:
        todo_item = todo.objects.get(id=todo_id)
    except todo.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "Todo not found"},
            status=404
        )

    todo_item.delete()

    return JsonResponse(
        {
            "success": True,
            "message": "Todo deleted"
        },
        status=200
    )
