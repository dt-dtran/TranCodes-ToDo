# Generated by Django 4.2 on 2023-05-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name="Note",
        ),
    ]