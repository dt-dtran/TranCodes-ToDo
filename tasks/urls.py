from django.urls import path
from tasks.views import create_task, list_task

app_name = "tasks"

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_task, name="show_my_tasks"),
]
