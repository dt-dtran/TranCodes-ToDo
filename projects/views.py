from django.shortcuts import render
from projects.models import *


# Create your views here.
def list_project(request):
    lists = Project.objects.all()
    context = {
        "lists": lists,
    }
    return render(request, "projects/list.html", context)
