from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name='Todos'),
    path("todos/edit", views.todos_edit, name="Todos_edit"),
]