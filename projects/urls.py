from django.urls import path
from projects.views import *

urlpatterns = [path("", list_projects, name="list_projects")]
