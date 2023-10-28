from django import forms
from .models import Task, TaskPhoto



class DatePickerInput(forms.DateInput):
    input_type = "date"

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completion_status']

        widgets = {
            "due_date": DatePickerInput(),
        }

class TaskPhotoForm(forms.ModelForm):
    class Meta:
        model = TaskPhoto
        fields = ['photo']
