from django.urls import path
from projects.views import *

urlpatterns = [path("", list_project, name="list_project")]
