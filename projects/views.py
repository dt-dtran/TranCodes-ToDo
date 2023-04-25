from django.shortcuts import render, get_object_or_404, redirect
from projects.models import *
from django.contrib.auth.decorators import login_required
from tasks.models import *
from projects.forms import *


# Create your views here.
@login_required
def list_projects(request):
    lists = Project.objects.filter(owner=request.user)
    context = {
        "lists": lists,
    }
    return render(request, "projects/list.html", context)


@login_required
def project_detail(request, id):
    detail = get_object_or_404(Project, id=id)
    context = {"detail": detail}
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {"form": form}
    return render(request, "projects/create.html", context)
