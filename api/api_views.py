from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class TaskViewSet(ModelViewSet):
    """
    ViewSet for Tasks
    """
    queryset = Task.objects.all().order_by('-last_updated')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


class LoginAPIView(APIView):
    """
    Logs in a user
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("Login successful")
        else:
            return Response("Invalid login", status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    """
    Logs a user out
    """
    def get(self, request):
        logout(request)
        return Response("Logout successful")
