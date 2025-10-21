from django.urls import path
from . import views

urlpatterns = [
    path("todo", views.ToDoView.as_view()),
    path("create_todo", views.CreateToDoView.as_view()),
    path("reminders", views.RemindersView.as_view()),
    path("create_reminders", views.CreateRemindersView.as_view()),

]