from django.urls import path
from projects.views import (
    list_projects,
    project_detail,
    create_project,
    start_project_detail,
    team_list,
    create_category,
    task_by_tag,
)

urlpatterns = [
    path("demo/", start_project_detail, name="demo"),
    path("list/", list_projects, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("create/category/", create_category, name="create_category"),
    path("team/", team_list, name="list_team"),
    path("tag/", task_by_tag, name="task_by_tag"),
]
