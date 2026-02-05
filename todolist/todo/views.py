from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (TodoCreateSerializer,
                        TodoListSerializer,
                        TodoDeleteSerializer,
                        TodoUpdateSerializer)

from .models import Todo
from .decorators import class_permission
from accounts.models import User
from .permissions import (is_jwt_authenticated,
                          can_create,
                          can_delete,
                          can_read,
                          can_update)

@class_permission(is_jwt_authenticated,can_create)
class AddTodoView(APIView):

    def post(self, request):
        
        serializer = TodoCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=request.user_id)

        serializer.save(user=user)

        request.session["last_action"] = "created todo"

        return Response({"message": "Todo created"},status=status.HTTP_200_OK)


@class_permission(is_jwt_authenticated, can_read)
class ListTodoView(APIView):

    def get(self, request):
        todos = Todo.objects.filter(user_id=request.user_id)
        serializer = TodoListSerializer(todos, many=True)

        return Response(serializer.data, status=200)

@class_permission(is_jwt_authenticated, can_update)
class UpdateTodoView(APIView):

    def put(self,request):
        data = request.data
        if not data:
            return Response({"id": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            todo = Todo.objects.get(id=data.get("id"), user_id=request.user_id)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=404)
        
        serializer = TodoUpdateSerializer(todo, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({"message": "Updated"},status=status.HTTP_200_OK)

@class_permission(is_jwt_authenticated, can_delete)
class DeleteTodoView(APIView):

    def delete(self, request):
        if not request.user_id:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TodoDeleteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        todo_id = serializer.validated_data["id"]

        try:
            Todo.objects.get(id=todo_id, user_id=request.user_id).delete()
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=404)

        return Response({"message": "Deleted"}, status=200)

