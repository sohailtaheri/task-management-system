from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics
from tms.models import ProjectModel, TaskModel
from tms.serializers import ProjectSerializer, TaskSerializer, UserSerializer

class BaseListView(APIView):
    """
    Abstract base class for listing and creating objects.
    """
    model = None
    serializer_class = None

    def get(self, request):
        objects = self.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ProjectList(BaseListView):
    """
    List all projects, or create a new project.
    """
    model            = ProjectModel
    serializer_class = ProjectSerializer

class TaskList(BaseListView):
    """
    List all tasks, or create a new task.
    """
    model            = TaskModel
    serializer_class = TaskSerializer

class BaseDetailView(APIView):
    """
    Abstract base class for retrieving, updating or deleting objects.
    """
    model = None
    serializer_class = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None
    def get(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return HttpResponse(status=404)
        serializer = self.serializer_class(obj)
        return JsonResponse(serializer.data)
    def put(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = self.serializer_class(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request, pk):
        obj = self.get_object(pk)
        if obj is None:
            return HttpResponse(status=404)
        obj.delete()
        return HttpResponse(status=204)

class ProjectDetail(BaseDetailView):
    """
    Retrieve, update or delete a project.
    """
    model            = ProjectModel
    serializer_class = ProjectSerializer

class TaskDetail(BaseDetailView):
    """
    Retrieve, update or delete a task.
    """
    model            = TaskModel
    serializer_class = TaskSerializer
    
class UserList(generics.ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):  
    """
    Retrieve, update or delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer