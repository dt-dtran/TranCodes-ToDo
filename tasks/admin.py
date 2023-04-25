from django.contrib import admin
from tasks.models import *


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "start_date",
        "due_date",
        "is_completed",
        "project",
        "assignee",
    )
