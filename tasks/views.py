from django.shortcuts import render, redirect
from tasks.forms import *
from tasks.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
        form.fields["assignee"].queryset = User.objects.filter(
            username=request.user
        )

    context = {"form": form}
    return render(request, "tasks/create_task.html", context)
