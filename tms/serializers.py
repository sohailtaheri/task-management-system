from rest_framework import serializers
from .models import TaskModel, ProjectModel
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TaskModel
        fields = [
            'id', 
            'title', 
            'created', 
            'modified', 
            'project', 
            'status', 
            'priority', 
            'due_date', 
            'created_by',
            'assigned_to'
        ]

        read_only_fields = ['created', 'modified', 'created_by']


class ProjectSerializer(serializers.ModelSerializer):
    
    tasks = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProjectModel
        fields = [
            'id', 
            'title', 
            'description', 
            'created',
            'modified',
            'owner',
            'tasks',
        ]
    
    

class UserSerializer(serializers.ModelSerializer):
    projects       = serializers.StringRelatedField(many=True, read_only=True)

    created_tasks  = TaskSerializer(many=True, read_only=True)
    assigned_tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'projects',
            'created_tasks',
            'assigned_tasks',
        ]

class UserSerializerPublic(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email',
        ]