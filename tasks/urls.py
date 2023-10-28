from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskPhotoDeleteView,
    TaskFilterView,
    TaskDetailAPIView, 
    TaskListAPIView,
    
)

app_name = "tasks"

urlpatterns = [
    
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/photo/delete/", TaskPhotoDeleteView.as_view(), name="task-photo-delete"),
    path('tasks/filter/', TaskFilterView.as_view(), name='task-list-filter'),

    path('api/tasks/', TaskListAPIView.as_view(), name='api-task-list'),
    path('api/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='api-task-detail'),

]

