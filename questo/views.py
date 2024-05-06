from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task


def index(request):
    context = {}
    context["tasks"] = Task.objects.all()
    return render(request, "questo/index.html", context)


def add_task(request):
    if "text" in request.POST:
        task = Task()
        task.text = request.POST["text"]
        task.priority = request.POST["priority"]
        task.save()
    return redirect('questo:index')


def change_status(request, task_id):
    if "status" in request.POST:
        task = Task.objects.get(pk=task_id)
        task.status = request.POST["status"]
        task.save()
    return HttpResponseRedirect(reverse('questo:index'))


def change_priority(request, task_id):
    if "priority" in request.POST:
        task = Task.objects.get(pk=task_id)
        task.priority = request.POST["priority"]
        task.save()
    return render(request, 'questo/detail.html', {'task': task})


def delete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('questo:index')


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'questo/detail.html', {'task': task})