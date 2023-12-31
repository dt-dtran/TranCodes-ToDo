# Generated by Django 4.2 on 2023-05-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_task_description_delete_note"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("Not Started", "Not Started"),
                    ("In Progress", "In Progress"),
                    ("Blocked", "Blocked"),
                    ("Complete", "Complete"),
                ],
                default="Not Started",
                max_length=200,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="tag",
            field=models.ManyToManyField(
                null=True, related_name="t_tags", to="tasks.tasktag"
            ),
        ),
    ]
