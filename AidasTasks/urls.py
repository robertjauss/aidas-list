from django.contrib import admin
from django.urls import path, include

from AidasTasks import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("task/crud/", views.task_crud_view, name="task_crud"),
    path("accounts/", include("django.contrib.auth.urls")),
]
