from django.contrib import admin
from .models import Task, TaskPhoto

class TaskAdmin(admin.ModelAdmin):
    list_display = ('assigned_user', 'title', 'due_date', 'priority', 'completion_status')
    ordering = ('priority',)

admin.site.register(Task, TaskAdmin)

admin.site.register(TaskPhoto)
