from django.db import models
from django.conf import settings

# Create your models here.
USER_MODEL = settings.AUTH_USER_MODEL


class ProjectCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(
        USER_MODEL,
        related_name="teams",
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )
    team = models.ForeignKey(
        Team,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )
    category = models.ManyToManyField(
        ProjectCategory,
        related_name="projects",
    )

    def __str__(self):
        return self.name


class ProjectUpdate(models.Model):
    class ProjectStatus(models.TextChoices):
        Green = "Green"
        Amber = "Amber"
        Red = "Red"

    project = models.ForeignKey(
        Project,
        related_name="updates",
        on_delete=models.CASCADE,
        null=True,
    )
    scope = models.CharField(
        max_length=50,
        null=True,
        choices=ProjectStatus.choices,
        default=ProjectStatus.Green,
    )
    schedule = models.CharField(
        max_length=50,
        null=True,
        choices=ProjectStatus.choices,
        default=ProjectStatus.Green,
    )
    cost = models.CharField(
        max_length=50,
        null=True,
        choices=ProjectStatus.choices,
        default=ProjectStatus.Green,
    )
    update = models.TextField(null=True)
