from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import TaskFilter

from .models import Task, TaskPhoto
from .forms import TaskForm, TaskPhotoForm

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(assigned_user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(assigned_user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('tasks:task-list')

    def form_valid(self, form):
        form.instance.assigned_user = self.request.user
        response = super().form_valid(form)

        try:
            photos = self.request.FILES.getlist('photos')
            for photo in photos:
                TaskPhoto.objects.create(task=self.object, photo=photo)
            messages.success(self.request, 'Task and Photo uploaded successfully.')
        except Exception as e:
            messages.error(self.request, f"Error uploading photos: {str(e)}")

        return response

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('tasks:task-list')

    def get_queryset(self):
        return Task.objects.filter(assigned_user=self.request.user)

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task-list')

    def get_queryset(self):
        return Task.objects.filter(assigned_user=self.request.user)
    
    
@method_decorator(login_required, name='dispatch')
class TaskPhotoDeleteView(View):
    def post(self, request, pk):
        task_photo = get_object_or_404(TaskPhoto, pk=pk)

        if task_photo.task.assigned_user != self.request.user:
            messages.error(request, 'Permission denied. You cannot delete this photo.')
            return redirect('tasks:task-detail', pk=task_photo.task.pk)

        try:
            task_photo.delete()
            messages.success(self.request, "Photo deleted successfully.")
        except Exception as e:
            messages.error(self.request, f"Error deleting photo: {str(e)}")

        return redirect('tasks:task-detail', pk=task_photo.task.pk)

@method_decorator(login_required, name='dispatch')
class TaskFilterView(FilterView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    paginate_by = 5



#..................API....................


class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
