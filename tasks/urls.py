from django.urls import path
from tasks.views import (
    create_task,
    list_task,
    update_task,
    task_detail,
)

app_name = "mytasks"

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_task, name="show_my_tasks"),
    path("mine/<int:id>/edit/", update_task, name="edit_tasks"),
    path("mine/<int:id>/detail/", task_detail, name="task_detail"),
]
