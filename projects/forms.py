from django.forms import ModelForm
from projects.models import (
    Project,
    Team,
    ProjectCategory,
    ProjectUpdate,
    USER_MODEL,
)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
            "team",
            "category",
        ]


class ProjectCategoryForm(ModelForm):
    class Meta:
        model = ProjectCategory
        fields = [
            "name",
        ]


class ProjectUpdatesForm(ModelForm):
    class Meta:
        model = ProjectUpdate
        fields = [
            "project",
            "scope",
            "schedule",
            "cost",
            "update",
        ]
