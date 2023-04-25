from django.shortcuts import render
from projects.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_projects(request):
    lists = Project.objects.filter(owner=request.user)
    context = {
        "lists": lists,
    }
    return render(request, "projects/list.html", context)
