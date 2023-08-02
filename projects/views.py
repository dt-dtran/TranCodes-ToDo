from django.shortcuts import render, get_object_or_404, redirect
from projects.models import (
    Project,
    ProjectCategory,
    ProjectUpdate,
    Team,
    USER_MODEL,
)
from django.contrib.auth.decorators import login_required
from projects.forms import (
    ProjectForm,
    ProjectCategoryForm,
    ProjectUpdatesForm,
)
from tasks.models import Task, TaskTag
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your views here.
def start_project_detail(request):
    detail = get_object_or_404(Project, id=1)
    context = {"detail": detail}
    return render(request, "projects/detail.html", context)


@login_required
def list_projects(request):
    lists = Project.objects.filter(owner=request.user)
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "lists": lists,
        "tasks": tasks,
    }
    return render(request, "projects/list.html", context)


@login_required
def project_detail(request, id):
    detail = get_object_or_404(Project, id=id)
    categories = detail.category.all()
    category_tasks = {}
    for category in categories:
        category_tasks[category] = detail.tasks.filter(category=category)
    context = {
        "detail": detail,
        "categories": categories,
        "category_tasks": category_tasks,
    }

    context = {"detail": detail, "categories": categories}
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {"form": form}
    return render(request, "projects/create.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ProjectCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectCategoryForm()

    context = {"form": form}
    return render(request, "projects/create_category.html", context)


@login_required
def team_list(request):
    teams = Team.objects.filter(members=request.user)
    context = {"teams": teams}
    return render(request, "projects/teams/team_list.html", context)


@login_required
def task_by_tag(request):
    user = request.user
    projects = Project.objects.filter(owner=user)
    tags = TaskTag.objects.all()

    task_data = {}
    for tag in tags:
        task_data[tag.tag] = {}
        for project in projects:
            tasks = Task.objects.filter(
                assignee=user, project=project, tag=tag
            )
            task_data[tag.tag][project.name] = tasks

    context = {"task_data": task_data}
    return render(request, "projects/task_by_tag.html", context)


@receiver(post_save, sender=Task)
def update_project_category(sender, instance, **kwargs):
    """
    Update the related project's categories based on the assigned task category
    """
    if instance.project:
        project = instance.project
        if instance.category not in project.category.all():
            project.category.add(instance.category)
