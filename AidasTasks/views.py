from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, QueryDict
from django.shortcuts import render
from django.views.generic import ListView

from api.models import Task


class HomeView(LoginRequiredMixin, ListView):
    template_name = "pages/home.html"
    model = Task
    context_object_name = "tasks"


def task_crud_view(request):
    if request.method == "POST":
        data = request.POST
        Task.objects.create(title=data.get("title"), notes=data.get("notes"))
        tasks = Task.objects.all()
        messages.success(request, "Task created")
        return render(request, "pages/home.html", {"tasks": tasks})

    if request.method == "PATCH":
        data = QueryDict(request.body)
        task = Task.objects.get(pk=data.get("id"))
        if title := data.get("title"):
            task.title = title
        if notes := data.get("notes"):
            task.notes = notes
        if completed := data.get("completed"):
            task.completed = False if completed == "True" else True
        task.save()
        tasks = Task.objects.all()
        return render(request, "pages/home.html", {"tasks": tasks})

    if request.method == "DELETE":
        data = request.GET
        task = Task.objects.get(pk=data.get("id"))
        task.delete()
        tasks = Task.objects.all()
        messages.success(request, "Task deleted")
        return render(request, "pages/home.html", {"tasks": tasks})

    return Http404
