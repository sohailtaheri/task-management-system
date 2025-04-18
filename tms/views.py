from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from tms.models import ProjectModel, TaskModel
from tms.serializers import ProjectSerializer, TaskSerializer
from django.contrib.auth.models import User

class ProjectList(APIView):
    """
    List all projects, or create a new project.
    """
    def get(self, request):
        projects = ProjectModel.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ProjectDetail(APIView):
    """
    Retrieve, update or delete a project.
    """
    def get_object(self, pk):
        try:
            return ProjectModel.objects.get(pk=pk)
        except ProjectModel.DoesNotExist:
            return None

    def get(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        serializer = ProjectSerializer(project)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return HttpResponse(status=404)
        project.delete()
        return HttpResponse(status=204)

class TaskList(APIView):
    """
    List all tasks, or create a new task.
    """
    def get(self, request):
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class TaskDetail(APIView):
    """
    Retrieve, update or delete a task.
    """
    def get_object(self, pk):
        try:
            return TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return HttpResponse(status=404)
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return HttpResponse(status=404)
        task.delete()
        return HttpResponse(status=204)
