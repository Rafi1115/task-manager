
from django.urls import path
from .views import register_view

app_name = "register"


# tasks/urls.py

urlpatterns = [

    path('', register_view, name='register'),
 
    # ... your other URL patterns ...
]
