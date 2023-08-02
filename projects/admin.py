from django.contrib import admin
from projects.models import Project, ProjectCategory, Team, ProjectUpdate


# Register your models here.
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
        "members_list",
        "category_list",
    )

    def members_list(self, obj):
        if obj.team:
            return ", ".join(
                [str(member) for member in obj.team.members.all()]
            )
        else:
            return "-"

    def category_list(self, obj):
        return ", ".join([str(name) for name in obj.category.all()])

    category_list.short_description = "Category"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "members_list",
    )

    def members_list(self, obj):
        return ", ".join([str(member) for member in obj.members.all()])

    members_list.short_description = "Members"
