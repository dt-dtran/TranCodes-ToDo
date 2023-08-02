from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.assignee = request.user
            task.save()
            return redirect("show_project", id=task.project.id)
    else:
        form = TaskForm()
        form.fields["assignee"].queryset = User.objects.filter(
            username=request.user
        )

    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def list_task(request):
    lists = Task.objects.filter(assignee=request.user)
    context = {
        "lists": lists,
    }
    return render(request, "tasks/tasks.html", context)


@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.is_completed = request.POST.get("is_completed") == "on"
            task = form.save()
            return redirect(reverse("show_project", args=[task.project.id]))
    else:
        form = TaskForm(instance=task)
    context = {"task": task, "form": form, "id": id}
    return render(request, "tasks/edit_task.html", context)


@login_required
def task_detail(request, id):
    detailed = get_object_or_404(Task, id=id)
    context = {"detailed": detailed}
    return render(request, "tasks/detailed.html", context)
