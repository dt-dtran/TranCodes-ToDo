from django.shortcuts import render, get_object_or_404
from projects.models import *
from django.contrib.auth.decorators import login_required
from tasks.models import *


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
