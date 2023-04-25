from django.contrib import admin
from projects.models import *


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )
