# Generated by Django 4.2 on 2023-05-03 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "projects",
            "0002_projecttag_team_projectupdate_project_tag_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="tag",
            field=models.ManyToManyField(
                related_name="projects", to="projects.projecttag"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="projects.team",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="members",
            field=models.ManyToManyField(
                related_name="teams", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
