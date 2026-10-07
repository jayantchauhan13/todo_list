from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by("completed", "-id")
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "todo/home.html", {"tasks": tasks, "form": form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect("home")

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")
