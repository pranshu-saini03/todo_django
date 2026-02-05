from django.urls import path
from .views import AddTodoView,ListTodoView,UpdateTodoView,DeleteTodoView

urlpatterns = [
    path("todos/",ListTodoView.as_view() ),
    path("todos/add/",AddTodoView.as_view()),
    path("todos/update/",UpdateTodoView.as_view() ),
    path("todos/delete/", DeleteTodoView.as_view()),
]
