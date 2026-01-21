from django.urls import path
from . import views

urlpatterns = [
    path("todos/", views.todo_list),
    path("todos/add/", views.add_todo),
    path("todos/update/<int:id>/", views.update_todo),
    path("todos/delete/<int:id>/", views.delete_todo),
]
