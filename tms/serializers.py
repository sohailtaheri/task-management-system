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
        def create(self, validated_data):
            return TaskModel.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.status = validated_data.get('status', instance.status)
            instance.priority = validated_data.get('priority', instance.priority)
            instance.due_date = validated_data.get('due_date', instance.due_date)
            instance.save()
            return instance


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = ProjectModel
        fields = [
            'id', 
            'title', 
            'description', 
            'created', 
            'created_by', 
            'tasks'
        ]

        def create(self, validated_data):
            tasks_data = validated_data.pop('tasks')
            project = ProjectModel.objects.create(**validated_data)
            for task_data in tasks_data:
                TaskModel.objects.create(project=project, **task_data)
            return project

        def update(self, instance, validated_data):
            tasks_data = validated_data.pop('tasks', None)
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.save()

            if tasks_data:
                for task_data in tasks_data:
                    task_id = task_data.get('id')
                    if task_id:
                        task = TaskModel.objects.get(id=task_id, project=instance)
                        task.title = task_data.get('title', task.title)
                        task.description = task_data.get('description', task.description)
                        task.status = task_data.get('status', task.status)
                        task.priority = task_data.get('priority', task.priority)
                        task.due_date = task_data.get('due_date', task.due_date)
                        task.save()
                    else:
                        TaskModel.objects.create(project=instance, **task_data)

            return instance