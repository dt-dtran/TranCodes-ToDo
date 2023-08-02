from django.forms import ModelForm
from tasks.models import Task
from django.forms.widgets import DateInput
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "description",
            "status",
            "priority",
            "category",
        ]
        widgets = {
            "start_date": DateInput(attrs={"type": "date"}),
            "due_date": DateInput(attrs={"type": "date"}),
            "is_completed": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }
