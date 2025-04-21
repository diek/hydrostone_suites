from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'task', 'annual_task', 'assigned_by',
            'task_details', 'date_started', 'date_completed'
        ]
