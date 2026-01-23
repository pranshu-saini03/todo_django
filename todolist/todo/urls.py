from django.urls import path
from . import views

urlpatterns = [
    path("todos/", views.list_todo),
    path("todos/add/", views.add_todo),
    path("todos/update/", views.update_todo),
    path("todos/delete/", views.delete_todo),
]
