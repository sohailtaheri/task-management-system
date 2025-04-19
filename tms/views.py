from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from tms.models import ProjectModel, TaskModel
from tms.serializers import ProjectSerializer, TaskSerializer, UserSerializer



class BaseListView(APIView):
    """
    Abstract base class for listing and creating objects.
    """
    model                  = None
    serializer_class       = None
    authentication_classes = [JWTAuthentication]
    permission_classes     = [permissions.IsAuthenticated]

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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskList(BaseListView):
    """
    List all tasks, or create a new task.
    """
    model            = TaskModel
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

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

class RegisterView(APIView):
    """
    Register a new user.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes     = [permissions.AllowAny]
    def post(self, request):
        data     = JSONParser().parse(request)
        username = data.get('username', None)
        password = data.get('password', None)
        email    = data.get('email', None)

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "Account created successfully!"}, status=status.HTTP_201_CREATED)