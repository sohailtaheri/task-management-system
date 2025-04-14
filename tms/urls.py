from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
] 