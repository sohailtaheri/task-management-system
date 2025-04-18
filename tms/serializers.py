from rest_framework import serializers
from .models import TaskModel, ProjectModel
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = [
            'id', 
            'title', 
            'description', 
            'created', 
            'modified', 
            'project', 
            'status', 
            'priority', 
            'due_date', 
            'created_by'
        ]

        read_only_fields = ['created', 'modified', 'created_by']


class ProjectSerializer(serializers.ModelSerializer):

    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ProjectModel
        fields = [
            'id', 
            'title', 
            'description', 
            'created',
            'modified',
            'created_by',
            'tasks',
        ]