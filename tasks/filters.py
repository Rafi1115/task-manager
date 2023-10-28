import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    created_at = django_filters.DateFilter(label='Created at (YYYY-MM-DD)', field_name='created_at', lookup_expr='date')
    due_date = django_filters.DateFilter(label='Due date (YYYY-MM-DD)', field_name='due_date', lookup_expr='date')
    priority = django_filters.ChoiceFilter(label='Priority', choices=Task.PRIORITY_CHOICES)
    completion_status = django_filters.BooleanFilter(
        field_name="completion_status",
        label="",
    )


    class Meta:
        model = Task
        fields = ['completion_status']
