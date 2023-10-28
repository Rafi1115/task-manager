from django.db import models
from accounts.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    completion_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskPhoto(models.Model):
    task = models.ForeignKey(Task, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='task_photos/')

    def __str__(self):
        return f"Photo for {self.task.title}"
