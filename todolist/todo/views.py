from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import todo

@csrf_exempt
def todo_list(request):
    todo_list=todo.objects.all()
    return JsonResponse({"success": True,
                          "data":list(todo_list.values())
                          },
                        status=200)

@csrf_exempt
def  add_todo(request):
    if request.method=="POST":
        data=json.loads(request.body)
        title=data.get("title")
        description=data.get("description")
        todo_item=todo.objects.create(title=title,description=description)
        return JsonResponse(
            {
                "success": True,
                "message": "Todo created",
                "todo_id": todo_item.id
            },
            status=201
        )

@csrf_exempt
def update_todo(request, id):
    if request.method=="PUT":
        try:
            todo_item=todo.objects.get(id=id)
        except todo.DoesNotExist:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Todo not found"
                },
                status=404
            )
        data=json.loads(request.body)
        todo_item.title=data.get("title")
        todo_item.description=data.get("description")
        todo_item.completed=data.get("completed", todo_item.completed)
        todo_item.save()
        return JsonResponse(
            {
                "success": True,
                "message": "Todo updated"
            },
            status=200
        )

@csrf_exempt
def delete_todo(request, id):
    if request.method=="DELETE":
        try:
            todo_item=todo.objects.get(id=id)
            todo_item.delete()
            return JsonResponse({
                "success":True,
                "message":"Todo deleted"
            },status=200
            )
        except todo.DoesNotExist:
            return JsonResponse({
                "success":False,
                "message":"Todo not found"
            },status=404
            )
# Create your views here.