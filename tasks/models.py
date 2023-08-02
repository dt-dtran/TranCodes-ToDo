from django.db import models
from projects.models import Project, USER_MODEL, ProjectCategory


# Create your models here.
class TaskTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        Not_started = "Not Started"
        In_progress = "In Progress"
        Blocked = "Blocked"
        Complete = "Complete"

    class TaskPriority(models.TextChoices):
        Urgent = "Urgent"
        High = "High"
        Moderate = "Moderate"
        Low = "Low"
        Blank = "-"

    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        USER_MODEL,
        related_name="tasks",
        null=True,
        on_delete=models.CASCADE,
    )
    description = models.TextField(null=True)
    status = models.CharField(
        max_length=200,
        null=True,
        choices=TaskStatus.choices,
        default=TaskStatus.Not_started,
    )
    priority = models.CharField(
        max_length=200,
        null=True,
        choices=TaskPriority.choices,
        default=TaskPriority.Blank,
    )
    category = models.ForeignKey(
        ProjectCategory,
        related_name="tasks",
        null=True,
        on_delete=models.SET_NULL,
    )
    tag = models.ManyToManyField(
        TaskTag,
        related_name="tasks",
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"
