import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import TodoItem
from .forms import Todo_completed_form

logging.basicConfig(
    filename='app.log',  # Specify the log file name
    level=logging.INFO,  # Set the logging level (e.g., INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Define the log message format
)

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "home.html")

def todos(request):
    if request.method == 'POST':
        todo_id = request.POST.get('id')
        is_completed = request.POST.get('completed') == 'on'
        add = request.POST.get('add_button')

        todo = get_object_or_404(TodoItem, id=todo_id)
        todo.completed = is_completed
        todo.save()

        return HttpResponseRedirect('/todos/')


    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def todos_edit(request):
    return render(request, "edit_todos.html")